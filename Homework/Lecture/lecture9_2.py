census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]
    
i = 0
total = 0
while i < (len(census) - 1):
    avg = ((census[i+1]-census[i])/census[i]) * 100
    i += 1
    total += avg

    
totalavg = total/(len(census) - 1)
print("Average = {:.1f}".format(totalavg) + "%")
