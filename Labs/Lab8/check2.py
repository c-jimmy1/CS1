# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:35:12 2022

@author: jc219
"""


def get_words(description):
    fixedSet = set()
    listwords = description.split()
    for word in listwords: 
        word = word.lower()
        for letter in word: 
            if letter.isalpha() == False: 
                word = word.replace(letter, "")
        if len(word) >= 4:
            fixedSet.add(word)
    return fixedSet

file1 = input("Enter a file name: ")
file1.strip()
print(file1)
fileopen1 = open(file1, "r")

file2 = input("Enter a second file name: ")
file1.strip()
print(file1)
fileopen2 = open(file2, "r")

clubinfo1 = fileopen1.read().strip().split('|')
description1 = clubinfo1[1]

clubinfo2 = fileopen2.read().strip().split('|')
description2 = clubinfo2[1]


s1 = get_words(description1)
s2 = get_words(description2)

print('Same words:', s1.intersection(s2))
print('\nUnique to {}: {}'.format(file1, s1.difference(s2)))
print('\nUnique to {}: {}'.format(file2, s2.difference(s1)))
