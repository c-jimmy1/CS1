# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 19:01:20 2022

@author: jc219
"""

#allows user to input a file name
inputfile = input('Enter the scores file: ')
inputfile = inputfile.strip()
print(inputfile)
#opens the file that the user inputs
scores = open(inputfile)

#allows user to input the output file name
outputfile = input('Enter the output file: ')
outputfile = outputfile.strip()
print(outputfile)
#opens the file to write
sortedscores = open(outputfile, 'w')

#reads all the scores, then strip and split \n so it only has the numbers
scores1 = scores.read()
scores1 = scores1.strip().split('\n')
#sort scores in integer format
scores1.sort(key = int)

#i is the index of the score (starts at -1 so 0 is included)
i = -1
for n in scores1:
    n = int(n)
    i += 1
    sortedscores.write('{:2d}: {:3d}\n'.format(i,n))

sortedscores.close()

    