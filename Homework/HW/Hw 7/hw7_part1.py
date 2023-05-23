# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 15:20:44 2022

@author: jimmy chen

This code is for hw 7 about dictionaries. 
We are creating an autocorrect that suggest the top three similar words given an incorrectly spelled one.
"""

def drop(wordDict, word, potential): # pass in the dictionary, the word from the for loop, and the potential list for the word
    
    # turning every letter into a string in a list (easier to manipulate lists)
    wordaslist = []
    for letter in word:
        wordaslist.append(letter)
        
    for x in range(len(word)):
        temp = wordaslist.copy() # creating a copy of the list
        temp.pop(x) # removing the letter at index x
        joined = ''.join(temp) # join the word back together
        if joined in wordDict: # if the word is in the dictionary
            potential.append(joined) #add to potential
        temp = wordaslist.copy() # reset list for next iteration
        
def insert(wordDict, word, potential):
    alphabet = [chr(num) for num in range(97, 123)] # chr converts nums to their corresponding unicode characters, in this case a-z lowercase
    
    wordaslist = []
    for letter in word:
        wordaslist.append(letter)
    
    ''' Double for loop to test inserting the entire alphabet at each index of the word, appends to potential if match '''
    for x in range(len(word)+1): # for x in range of the length of the word + 1
        temp = wordaslist.copy()
        for y in range(len(alphabet)):
            temp.insert(x, alphabet[y])
            joined = ''.join(temp)
            if joined in wordDict:
                potential.append(joined)
            temp = wordaslist.copy()

def swap(wordDict, word, potential):
    for x in range(len(word)-1): # -1 because last index can't be swapped with anything
        original = word[x] # the original letter is word[x]
        initial = word # defining the initial word to be reset later
        word = word[:x] + word[x+1] + word[x+1:] # every letter before index x + the letter at the next index + the rest of the letters
        word = word[:x+1] + original + word[x+2:] # every letter before the index + original letter + every letter after
        if word in wordDict:
            potential.append(word)
        word = initial
    
def replace(wordDict, keyDict, word, potential):
    wordaslist = []
    for letter in word:
        wordaslist.append(letter) # turning letters into indices in a list

    for x in range(len(word)):
        for key in keyDict: # for every key letter in the dictionary
            temp = wordaslist.copy()
            listneighbor = keyDict[key] # the list of neighbors of a specific letter
            tempindex = temp[x] # temporary index of letter
            if tempindex == key: # if the letter during each iteration matches the key
                for y in range(len(listneighbor)): # loop through the list of neighbors
                    temp.pop(x) # deletes the letter at index x
                    temp.insert(x, listneighbor[y]) # insert at index x the neighboring key
                    joined = ''.join(temp)
                    if joined in wordDict: # if word matches, append to potential
                        potential.append(joined)
                    temp = wordaslist.copy()

''' Removing duplicates and sorting by greatest freq to least '''
def sort(wordDict, potential):
    setPotential = set(potential)
    sortedvalues = [] # sorted values has the list of (key and values)
    for key, value in wordDict.items(): # for every key, value in the dictionary
        for words in setPotential: # for every word in the potential words
            if key == words: # if the key, aka the word, matches the word in the potential, create a tuple with the freq first
                tuples = (value, key)
                sortedvalues.append(tuples)
                sortedvalues.sort(reverse = True)
    return sortedvalues
    

''' reading and putting words and freq into a dictionary '''
dict_file = input("Dictionary file => ").strip()
print(dict_file)
fileDopen = open(dict_file, 'r', encoding = "utf-8")

wordDict = dict() # initiating a dictionary
for line in fileDopen: #for every line in the dictionary file
    both = line.strip().split(',') # splitting each line by comma, which separates the word and freq
    word = both[0].strip()
    freq = both[1].strip()
    wordDict[word] = freq # setting every word to their freq in a dictionary


''' reading and putting all input words into a list '''
input_file = input('Input file => ').strip()
print(input_file)
fileIopen = open(input_file, 'r', encoding = 'utf-8')
input_words = fileIopen.read().split() # list of input words


''' reading and putting all keys with neighbors into a dictionary '''
keyboard_file = input('Keyboard file => ').strip()
print(keyboard_file)
fileKopen = open(keyboard_file, 'r', encoding = 'utf-8')

keyDict = dict()
for line in fileKopen:
    allLetters = line.strip().split(' ')
    first = allLetters[0]
    neighbors = []
    for letter in allLetters:
        if letter != first:
            neighbors.append(letter)
    keyDict[first] = neighbors
    
    
''' autocorrecting '''
for word in input_words:
    potential = [] # list where corrected words are appended to for every function, resets at every word in input_words
    spaceslength = 15 - len(word) # to create the spacing for printing
    spaces = spaceslength * ' '
    if word in wordDict: # if the word is in the dictionary
        print('{}{} -> FOUND'.format(spaces, word)) # print found
    elif word not in wordDict: # else if it is not in the dictionary...
        '''call functions to append valid words in the potential list'''
        drop(wordDict, word, potential)
        insert(wordDict, word, potential)
        replace(wordDict, keyDict, word, potential)
        swap(wordDict, word, potential) 
        
        sortedvalues = sort(wordDict, potential) # returns the list of freq and word from largest to smallest
        if len(potential) == 0: # if no potential words
            print('{}{} -> NOT FOUND'.format(spaces, word))
        elif len(sortedvalues) == 1:
            largest = sortedvalues[0][1] # largest if the word with largest
            print('{}{} -> FOUND{:3d}:  {}'.format(spaces, word, len(set(potential)), largest))

        elif len(sortedvalues) == 2: # if two words print largest and second largest
            largest = sortedvalues[0][1]
            second = sortedvalues[1][1]
            print('{}{} -> FOUND{:3d}:  {} {}'.format(spaces, word, len(set(potential)), largest, second))

        else: # else print the largest 3
            largest = sortedvalues[0][1]
            second = sortedvalues[1][1]
            third = sortedvalues[2][1]
            print('{}{} -> FOUND{:3d}:  {} {} {}'.format(spaces, word, len(set(potential)), largest, second, third))