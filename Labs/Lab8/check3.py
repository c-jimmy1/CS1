# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:57:25 2022

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

sclub = input('Enter a file with a single club: ')
sclub.strip()
print(sclub)
sclubopen = open(sclub, "r")
clubinfo1 = sclubopen.read().strip().split('|')
description1 = clubinfo1[1]

all_clubsopen = open('allclubs.txt', 'r')
all_clubs = all_clubsopen.read().strip().split('\n')
s1 = get_words(description1)

listDiff = []


for club in all_clubs:
    club_info = club.split('|')
    description2 = club_info[1]
    setClub = get_words(description2)
    if setClub != s1:
        x = s1.intersection(setClub)
        listDiff.append((len(x), club_info[0]))
        
listDiff.sort()
listDiff.sort(reverse=True)

top5 = [listDiff[0], listDiff[1], listDiff[2], listDiff[3], listDiff[4]]

print(top5)