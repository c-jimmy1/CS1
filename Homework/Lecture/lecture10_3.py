co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
    
avg = sum(co2_levels)/len(co2_levels)
co2_levels.sort()

#sum is the total number of numbers above avg
sum = 0

for num in co2_levels:
    if num > avg:
        sum += 1
        
print("Average: {:.2f}".format(avg))
print("Num above average: {:.0f}".format(sum))  