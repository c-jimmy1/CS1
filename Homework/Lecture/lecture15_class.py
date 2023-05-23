# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:16:15 2022

@author: jc219
"""
import time

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
start = time.time()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
print('This took {:.3f} seconds'.format(time.time()-start))