import lab06_util

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



def verify_board(board):
    r = 0
    count = 0
    while r < len(board):
        c = 0
        while c < len(board[0]):
            if(board[r][c].count('.') > 0):
                count+=1
            c+=1
        r+=1
    
    if count == 0:
        return True
    return False

file_name = input('Enter the name of the file: ')
print(file_name)

bd = lab06_util.read_sudoku(file_name)


exit = True
while(exit):
    isSolved = False
    i = 0
    counter = 0
    while i < len(bd):
        j=0
        while j < len(bd[0]):
            temp = str(bd[i][j])
            bd[i][j] = '.'
            if(ok_to_add(i,j,temp,bd) == False):
                counter +=1
            j+=1
        i+=1
    if counter == 0:
        isSolved = True        
    if counter  > 0:
        print("Board isn't complete")
    if(verify_board(bd)):
        if(isSolved):
            print("Board is complete")
            exit = False
            break

    row = int(input("Enter the row: "))
    print(row)
    col = int(input("Enter the column: "))
    print(col)
    value = int(input("Enter a value: "))
    print(value)

    r = 0
    c= 0
    array = []

    pri = ''
    print(ok_to_add(row, col, value, bd))

    while r < len(bd):
        if r ==0:
            pri+='-------------------------'
        pri +='\n'
        temp = []
        while c < (len(bd[0])):        
            if c % 3 == 0:
                pri +='|'+ ' '+str(bd[r][c]) +' ' 
                temp.append((r,c))
            
            else:
                pri += str(bd[r][c])+ ' '
                temp.append((r,c))
                if(c == 8):
                    pri +='|'
            c+=1
        c=0
        r+=1
        array.append(temp)
        temp = []
        if(r % 3 ==0):
            pri +='\n-------------------------'

    print(pri)
    