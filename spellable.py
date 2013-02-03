#!/usr/bin/env python

'''
See https://github.com/denis-ryzhkov/shortcom/blob/master/README.md

spellable.py for
shortcom version 0.0.2
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>
MIT License, see http://opensource.org/licenses/MIT
'''

#### config

chars  = 'bcdfghjklmnpqrstvwxz'
max_quantity = 2

available_path = 'available.txt'
spellable_path_format = 'spellable-{quantity}.txt'

#### code

for quantity in range(1, max_quantity + 1):

    available_file = open(available_path, 'r')
    spellable_file = open(spellable_path_format.format(quantity=quantity), 'w')

    for line in available_file:
        stones = 0
        for char in line:
            if char in chars:
                stones += 1
            else:
                stones = 0
            if stones > quantity:
                break
        if stones > quantity:
            continue
        spellable_file.write(line)

    available_file.close()
    spellable_file.close()
