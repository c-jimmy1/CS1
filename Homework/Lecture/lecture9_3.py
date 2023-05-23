intlist = []
value = int(input("Enter a value (0 to end): "))
print(value)

#adds the first value to the list
intlist.append(value)

#creates a loop that prompts the user to input numbers into list until 0 is inputted
#when the user inputs 0 the loops stop because condition is met
while value != 0:    
    value = int(input("Enter a value (0 to end): "))
    print(value)
    intlist.append(value)

intlist.pop(len(intlist)-1)
avg = sum(intlist)/len(intlist)

print("Min:", min(intlist))
print("Max:", max(intlist))
print("Avg: {:.1f}".format(avg))