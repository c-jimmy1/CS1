# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:05:33 2022

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
fileopen = open(file1, "r")
clubinfo = fileopen.read().strip().split('|')

description = clubinfo[1]
print("\nFile {} {} words".format(file1, len(get_words(description))))
print(get_words(description))
