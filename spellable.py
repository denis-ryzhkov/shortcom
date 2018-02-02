#!/usr/bin/env python

'''
See https://github.com/denis-ryzhkov/shortcom/blob/master/README.md

spellable.py for
shortcom version 0.1.3
Copyright (C) 2013-2018 by Denis Ryzhkov <denisr@denisr.com>
MIT License, see http://opensource.org/licenses/MIT
'''

#### config

consonants  = 'bcdfghjklmnpqrstvwxz'
digraphs = set('sc ng ch ck gh ph rh sh th wh zh wr'.split())  # https://en.wikipedia.org/wiki/Digraph_(orthography)#English

available_path = 'available.txt'
spellable_path_format = 'spellable-{quantity}.txt'
max_quantity = 2

#### code

for quantity in range(1, max_quantity + 1):
    available_file = open(available_path, 'r')
    spellable_file = open(spellable_path_format.format(quantity=quantity), 'w')

    for line in available_file:
        stones = 0
        prev_char = ''

        for char in line:
            if char in consonants:
                if prev_char + char not in digraphs:
                    stones += 1
            else:
                stones = 0

            prev_char = char

            if stones > quantity:
                break

        if stones > quantity:
            continue

        spellable_file.write(line)

    available_file.close()
    spellable_file.close()
