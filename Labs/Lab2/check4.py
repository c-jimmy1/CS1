import math

first = input("Please enter your first name: ")
last = input("Please enter your last name: ") + "!"
prompt = ("Hello,")
maximum = (max(len(first), len(last), len(prompt)) + 6)

space = maximum - (len(prompt) + 5)
space2 = maximum - (len(first) + 5)
space3 = maximum - (len(last) + 5)

print("*"*maximum)
print("*"*2, prompt + space*" " + "*"*2)
print("*"*2, first + space2*" " + "*"*2)
print("*"*2, last + space3*" " + "*"*2)
print("*"*maximum)
