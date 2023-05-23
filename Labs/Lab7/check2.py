def parse_line(string):
    if(string.count("/")>=3):
        text1=string[::-1].partition("/")
        text2 = text1[2].partition("/")
        text3 = text2[2].partition("/")
        if (text1[0].isdigit() == True and text2[0].isdigit() == True and text3[0].isdigit() == True):
            tup = (int(text3[0][::-1]), int(text2[0][::-1]), int(text1[0][::-1]), text3[2][::-1])
            return tup
        else:
            return None
    else:
        return None
def get_line(fname, parno, lineno):
    f = open((str(fname) + '.txt'), encoding = 'utf8')
    line = f.readlines()
    count = 0
    nl_count = 1
    ans = ""
    
    while count < len(line):
        if(nl_count == (parno)):
            find_line = count + lineno - 1
            if find_line >= len(line):
                print("ERROR")
                return
            ans = line[find_line].rstrip()
            break

        if(count != 0 and line[count] == '\n' and line[count-1] != '\n'):
            nl_count +=1
            while count < len(line) and line[count] == '\n':
                count += 1
            continue
        count += 1
    f.close()
    return ans

filename = int(input("Please enter the file number ==> "))
paragraph = int(input("Please enter the line number ==> "))
line = int(input("Please enter the line number ==> "))

print(get_line(filename, paragraph, line))