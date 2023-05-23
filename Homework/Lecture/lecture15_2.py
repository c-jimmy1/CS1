# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:56:21 2022

@author: jc219
"""

file = input('Data file name: ')
file = file.strip()
print(file)

prefix = input('Prefix: ')
prefix = prefix.strip()
print(prefix)

names = set()
for line in open(file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    fullname = words[0].strip().split(',')
    lastname = fullname[0]
    if not lastname in names:
        names.add(lastname)

total = 0
for x in names:
    if x.startswith(prefix) == True:
        total += 1    

print('{} last names'.format(len(names)))
print('{} start with {}'.format(total, prefix))