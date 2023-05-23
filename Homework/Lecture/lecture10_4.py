co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, 348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
    
p = input("Enter the fraction: ")
print(p)
p = float(p)

x = range(0, len(co2_levels))
for n in x:
    num = co2_levels[n]
    co2_levels.pop(n)
    co2_levels.insert(n, num * (1 + p))
    
co2_levels.sort()
print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))