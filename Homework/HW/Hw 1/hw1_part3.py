import math

character = input("Enter frame character  ==> ")
print(character)
character = character.strip()

height = (input("Height of box ==> "))
print(height)
height = height.strip()

width = (input("Width of box ==> "))
print(width)
width = width.strip()
    
totalChar = len(width) + len(height) + 1

height = int(height)
width = int(width)

totalSpace = width - 2 - totalChar
leftSpace = math.floor((totalSpace/2))
rightSpace = totalSpace - leftSpace

totalVertical = height - 3
upSpace = math.floor((totalVertical/2))
downSpace = totalVertical - upSpace

print("\nBox:")
print(character * width)
print((character + " " * (width - 2) + character + "\n") * (upSpace - 1) + (character + " " * (width - 2) + character))
print(character + " " * leftSpace + str(width) + "x" + str(height) + " " * rightSpace + character)
print((character + " " * (width - 2) + character + "\n") * (downSpace - 1) + (character + " " * (width - 2) + character))
print(character * width)
 
