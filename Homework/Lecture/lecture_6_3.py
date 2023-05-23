num1 = input("Enter the first number: ")
print(num1)
num2 = input("Enter the second number: ")
print(num2)


if float (num1) > 10 and float (num2) > 10:
    print("Both are above 10.")
elif float(num1) < 10 and float(num2) < 10:
    print("Both are below 10.")
    
avg = ((float(num1)+float(num2))/2)
print("Average is {:.2f}".format(avg))
