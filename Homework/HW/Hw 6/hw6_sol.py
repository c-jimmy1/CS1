# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:25:25 2022

@author: jc219
"""

def parse(listf):
    fixedList = []
    
    for word in listf: #for every string in the lists
        for letter in word: #for every character in string
            word = word.lower()
            if letter.isalpha() == False: #if the character isn't a letter...
                word = word.replace(letter, "") #replace letter with a empty character
        fixedList.append(word) #append fixed words to a new list   
        
        while("" in fixedList):
            fixedList.remove("") #remove all empty strings           
    return fixedList


def removeStop(nonFiltered, listStop): #pass in the nonFiltered list as well as the txt file with all the stop words
    filteredWords = []
    
    for word in nonFiltered: #for every word in the nonFiltered list
        if word not in listStop: #if the word isn't a part of list of stop words
            filteredWords.append(word) #add that word to the new list without stop words       
    return filteredWords

def avgWordLength(setWords):
    i = 0 #start count at 0
    for x in setWords: #for every word in the set of words
        i += len(x) #iterate the length of the word to i every loop
        avgLength = float(i)/len(setWords) #calculate the total num of characters divided by the total number of words
    return avgLength        

def longestWord(setfiltered): #finding the longest word to use for indexing when looping
    total_lengths = []
    for word in setfiltered: #for every word in the set of words
        length = len(word) #find length of each word
        total_lengths.append(length) #append each word to new list
    return max(total_lengths) #return the max of the list, which is the longest word

def wordPairs(filtered, max_sep): #finding wordPairs
    listPairs = [] #list of pairs
    for i in range(len(filtered)): #for i in range of the length of filtered
        for j in range(i+1,len(filtered)): #starts the loop at the number after i so j doesnt = i
            if j-i <= max_sep: #if j-i is less than the max_sep
                wordpair = (filtered[i], filtered[j])
                sortedpair = tuple(sorted(wordpair)) #sort the words then make it a tuple again
                listPairs.append(sortedpair) #add the tuple to the list of pairs
    return listPairs


def similarity(listSets, listSets2):
    #The below finds the smaller length of the two lists for indexing
    if len(listSets) < len(listSets2):
        smallerlength = len(listSets)
    elif len(listSets) > len(listSets2):
        smallerlength = len(listSets2)
    else:
        smallerlength = len(listSets)
        
    #The below finds the larger length of the two lists for indexing
    if len(listSets) > len(listSets2):
        largerlength = len(listSets)
    elif len(listSets) < len(listSets2):
        largerlength = len(listSets2)
    else:
        largerlength = len(listSets)
    
    listJaccard = [] #total list of jaccards in order
    for i in range(0, smallerlength): #for i in range of the smaller length
        listSets[i] #first set of distinct pairs for first file
        listSets2[i] #first set of distinct pairs for second file
        intersection = listSets[i].intersection(listSets2[i])
        union = listSets[i].union(listSets2[i])
        if len(union) == 0: #if the numerator, or the union is 0
            jaccard = 0 #the the jaccard is 0
            listJaccard.append(jaccard)
        else:
            jaccard = len(intersection)/len(union) #else find the ratio
            listJaccard.append(jaccard)
    for i in range(smallerlength + 1, largerlength + 1): #for all the sets out of range
        listJaccard.append(0) #make them 0 because it has nothing to compare to
    
    return listJaccard


file1 = input("Enter the first file to analyze and compare ==> ")
file1.strip()
print(file1)

file2 = input("Enter the second file to analyze and compare ==> ")
file2.strip()
print(file2)

max_sep = int(input("Enter the maximum separation between words in a pair ==> "))
print(max_sep)



''' EVALUATING DOCUMENT 1 '''

f = open(file1, "r", encoding = 'utf-8') #opening the file to read
listf = f.read().split() #reads and splits the file into individual strings
stopf = open("stop.txt", "r", encoding = 'utf-8') #opening the stop file to read
listStop = stopf.read().split() #reads and splits the file into individual strings

nonFiltered = parse(listf) #nonfiltered list is the list of words that have no nums but still has stop words
filtered = removeStop(nonFiltered, parse(listStop)) #filtered list is list of words with the stop words removed (listStop needs to be parsed to remove apostrophies)
setfiltered = set(filtered)

print('\nEvaluating document', file1)
print('1. Average word length: {:.2f}'.format(avgWordLength(filtered)))
print('2. Ratio of distinct words to total words: {:.3f}'.format(len(setfiltered)/len(filtered)))
print('3. Word sets for document {}:'.format(file1))

listLengths = [] #list of lists containing words sorted in length
longest = longestWord(setfiltered) #find the longest word, to use for indexing when looping
for i in range(1, longest + 1): #longest + 1, loops including longest
    tempList = [] #templist resets every loop
    for words in setfiltered: #for every word in the set of words
        if len(words) == i: #if the length of words is equal to the index at the moment
            tempList.append(words) #add the word to the temporary list
    tempList.sort() #sort the temporary list
    listLengths.append(tempList) #add the temporary list to listLengths

i = 1 #start iteration at 1
for lists in listLengths: #for each list in the listLengths
    if len(lists) >= 6: #if there are more than 6 words in the list...
        print('{:4d}:{:4d}: {} {} {} ... {} {} {}'.format(i, len(lists), lists[0], lists[1], lists[2], lists[-3], lists[-2], lists[-1]))
    elif len(lists) <= 6 and len(lists) > 0: #if there are less than 6 words in the list...
        print('{:4d}:{:4d}:'.format(i, len(lists)), end = '')
        for word in lists: #for every word in list, add it to the end of the print statement from before
            print(' ' + word, end = '')
        print()
    else: #else print 0:
        print('{:4d}:{:4d}:'.format(i, len(lists)))
    i += 1
    
pairsnonFilter = wordPairs(filtered, max_sep)
pairsFilter = set(pairsnonFilter)
pairsFilter = sorted(pairsFilter)
print('4. Word pairs for document {}'.format(file1))
print('  {} distinct pairs'.format(len(pairsFilter)))

if len(pairsFilter) > 10: #if the length of the filtered pairs is greater than 10
    for i in range(0, 5): #printing first 5
        print('  {} {}'.format(pairsFilter[i][0], pairsFilter[i][1]))
    print('  ...')
    for i in range(-5, 0): #printing last 5
        print('  {} {}'.format(pairsFilter[i][0], pairsFilter[i][1]))
elif len(pairsFilter) <= 10 and len(pairsFilter) > 0: #else if the length of the filtered pairs if less than 10
    for pairs in pairsFilter: #printing all since it's less than 10 pairs
        print('  {} {}'.format(pairs[0], pairs[1]))

print("5. Ratio of distinct word pairs to total: {:.3f}".format(len(pairsFilter)/len(pairsnonFilter)))



''' EVALUATING DOCUMENT 2 '''

f2 = open(file2, "r", encoding = 'utf-8')
listf2 = f2.read().split()

nonFiltered2 = parse(listf2)
filtered2 = removeStop(nonFiltered2, parse(listStop))
setfiltered2 = set(filtered2)

print('\nEvaluating document', file2)
print('1. Average word length: {:.2f}'.format(avgWordLength(filtered2)))
print('2. Ratio of distinct words to total words: {:.3f}'.format(len(setfiltered2)/len(filtered2)))
print('3. Word sets for document {}:'.format(file2))


listLengths2 = [] #list of lists containing words sorted in length
longest2 = longestWord(setfiltered2) #find the longest word, to use for indexing when looping
for i in range(1, longest2 + 1): #longest + 1, loops including longest
    tempList2 = [] #templist resets every loop
    for words in setfiltered2: #for every word in the set of words
        if len(words) == i: #if the length of words is equal to the index at the moment
            tempList2.append(words) #add the word to the temporary list
    tempList2.sort() #sort the temporary list
    listLengths2.append(tempList2) #add the temporary list to listLengths
    
j = 1 #start iteration at 1
for lists in listLengths2: #for each list in the listLengths
    if len(lists) >= 6: #if there are more than 6 words in the list...
        print('{:4d}:{:4d}: {} {} {} ... {} {} {}'.format(j, len(lists), lists[0], lists[1], lists[2], lists[-3], lists[-2], lists[-1]))
    elif len(lists) <= 6 and len(lists) > 0: #if there are less than 6 words in the list...
        print('{:4d}:{:4d}:'.format(j, len(lists)), end = '')
        for word in lists: #for every word in list, add it to the end of the print statement from before
            print(' ' + word, end = '')
        print()
    else: #else print 0:
        print('{:4d}:{:4d}:'.format(j, len(lists)))
    j += 1

pairsnonFilter2 = wordPairs(filtered2, max_sep)
pairsFilter2 = set(pairsnonFilter2)
pairsFilter2 = sorted(pairsFilter2)
print('4. Word pairs for document {}'.format(file2))
print('  {} distinct pairs'.format(len(pairsFilter2)))

if len(pairsFilter2) > 10: #if the length of the filtered pairs is greater than 10
    for i in range(0, 5): #printing first 5
        print('  {} {}'.format(pairsFilter2[i][0], pairsFilter2[i][1]))
    print('  ...')
    for i in range(-5, 0): #printing last 5
        print('  {} {}'.format(pairsFilter2[i][0], pairsFilter2[i][1]))
elif len(pairsFilter2) <= 10 and len(pairsFilter2) > 0: #else if the length of the filtered pairs if less than 10
    for pairs in pairsFilter2: #printing all since it's less than 10 pairs
        print('  {} {}'.format(pairs[0], pairs[1]))

print("5. Ratio of distinct word pairs to total: {:.3f}".format(len(pairsFilter2)/len(pairsnonFilter2)))



''' SUMMARY COMPARISON '''

print('\nSummary comparison')

if avgWordLength(filtered) > avgWordLength(filtered2): #if the length is larger on the first file
    print('1. {} on average uses longer words than {}'.format(file1, file2))
else:
    print('1. {} on average uses longer words than {}'.format(file2, file1))

'''the three lines below is the jaccard equation'''
intersection = setfiltered.intersection(setfiltered2)
union = setfiltered.union(setfiltered2)
jaccardAll = len(intersection)/len(union)

print('2. Overall word use similarity: {:.3f}'.format(jaccardAll))
print('3. Word use similarity by length:')

'''code from line 239 to 247 makes each list of words with the same word lengths into a set and add it back to a list'''
listSets = []
for lists in listLengths:
    sets = set(lists)
    listSets.append(sets)

listSets2 = []
for lists in listLengths2:
    sets = set(lists)
    listSets2.append(sets)

indexing2 = 1 #indexing for printing through for loop
similarities = similarity(listSets, listSets2) #calls the similarity function to find the jaccards between all the word lengths
for jaccard in similarities: #for each jaccard in the list of similarities
    print('{:4d}: {:.4f}'.format(indexing2, jaccard))
    indexing2 += 1

#makes each list of pairs into sets
setPair = set(pairsFilter)
setPair2 = set(pairsFilter2)

#calculate jaccard between the sets
pairsinter = setPair.intersection(setPair2)
pairsunion = setPair.union(setPair2)
jaccardpairs = len(pairsinter)/len(pairsunion)
print('4. Word pair similarity: {:.4f}'.format(jaccardpairs))
