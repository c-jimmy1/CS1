# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:55:43 2022

@author: jc219
"""

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

most_appear = max(list(counts.values()))

for key, value in counts.items():
        if most_appear == value:
            print('{} appears most often: {} times'.format(key, counts.get(key)))

i = 0
for key, value in counts.items():
        if value == 1:
            i += 1

print(i, 'people appear once')