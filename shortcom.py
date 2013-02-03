#!/usr/bin/env python

'''
See https://github.com/denis-ryzhkov/shortcom/blob/master/README.md

shortcom version 0.0.2
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>
MIT License, see http://opensource.org/licenses/MIT
'''

#### config

prefix = 'my'
chars = 'abcdefghijklmnopqrstuvwxyz'
quantity = 2
postfix = 'x.com'
skip_until = None

command_format = 'whois -h whois.verisign-grs.com -H ={domain}'
taken_substring = 'Registrar: '
available_substring = 'No match for "'
sleep_seconds = 0.5

taken_path = 'taken.txt'
available_path = 'available.txt'
error_path = 'error.txt'

#### code

from itertools import product
from time import sleep
from subprocess import Popen, PIPE

taken_file = open(taken_path, 'a')
available_file = open(available_path, 'a')

for domain in product(*([chars] * quantity)):
    domain = prefix + ''.join(domain) + postfix

    if skip_until:
        if domain == skip_until:
            skip_until = None
        else:
            continue

    stdout, stderr = Popen(command_format.format(domain=domain), shell=True, stdout=PIPE, stderr=PIPE).communicate()
    output = stdout + stderr

    if taken_substring in output:
        is_taken = True

    elif available_substring in output:
        is_taken = False

    else:
        error_file = open(error_path, 'w')
        error_file.write(domain + '\n')
        error_file.write(output)
        error_file.close()
        print(domain + ' - error response:')
        print(output)
        exit(1)

    print(domain + ' ' + ('is taken' if is_taken else 'is available'))

    output_file = taken_file if is_taken else available_file
    output_file.write(domain + '\n')
    output_file.flush()

    sleep(sleep_seconds)

for output_file in taken_file, available_file:
    output_file.close()
