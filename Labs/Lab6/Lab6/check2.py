def ok_to_add(row, column, value, bd):
    for x in range(0,9):
        if value == bd[row][x]:
            return False
        
    for y in range(0,9):
        if value == bd[y][column]:
            return False
 

    newrow = row // 3
    newcolumn = column // 3
    
    for x in range(0,3):
        for y in range(0,3):
            if value == bd[newrow * 3 + x][newcolumn * 3 + y]:
                return False
    return True

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]


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

row = int(input('Enter a row: '))
column = int(input('Enter a column: '))
value = input('Enter the value: ')

print(ok_to_add(row, column, value, bd))