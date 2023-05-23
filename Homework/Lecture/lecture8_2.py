values = [14, 10, 8, 19, 7, 13]

enter1 = input("Enter a value: ")
print(enter1)
enter2 = input("Enter another value: ")
print(enter2)

enter1 = int(enter1)
enter2 = int(enter2)

values.append(enter1)
values.insert(2, enter2)

#prints the integers at index 3 and index -
print(values[3], values[-1])

#prints difference and average, using .1f to round to the nearest 10
print('Difference:', (max(values) - min(values)))
print('Average: {:.1f}'.format((sum(values) / len(values))))

#sorts the list to calculate median
values.sort()

median = (values[3] + values[4])/2
print('Median:', median)
