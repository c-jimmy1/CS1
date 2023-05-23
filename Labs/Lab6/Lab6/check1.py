bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

'''
print(len(bd)) #total num of lists
print(len(bd[0])) #total number of characters in the list of the list
print(bd[0][0]) #first value of the character
print(bd[8][8]) #last character
'''

line = ''
for x in range(0,9):
    if x % 3 == 0:
        line = line + '\n-------------------------'
    line = line + '\n'
    for y in range(0,9):
        if y % 3 == 0:
            line = line + '| '
        line = line + bd[x][y] + ' '
        if y == 8:
            line = line + '|'            
line = line + '\n-------------------------'
print(line)


    
