def skew(time1, time2, time3, time4, time5):
    avg = (time1+time2+time3+time4+time5)/5
    var = (time1-avg)**2 + (time2-avg)**2 + (time3-avg)**2 + (time4-avg)**2 + (time5-avg)**2
    var /= 5
    skew = (time1-avg)**3 + (time2-avg)**3 + (time3-avg)**3 + (time4-avg)**3 + (time5-avg)**3
    skew /= 5
    skew = skew/var**3**0.5
    return skew

def maxMin(name, time1, time2, time3, time4, time5):
    maximum = max(time1, time2, time3, time4, time5)
    minimum = min(time1, time2, time3, time4, time5)
    avg = ((time1 + time2 + time3 + time4 + time5) - maximum - minimum) / 3
    print("{}'s stats-- min: {:d}, max: {:d}, avg: {:.2f}".format(name, minimum, maximum, avg))
    
print("{0}'s running times have a skew of {1:.2f}".format("Stan",skew(34, 34, 35, 31, 29)))
print("{0}'s running times have a skew of {1:.2f}".format("Kyle",skew(30, 31, 29, 29, 28)))
print("{0}'s running times have a skew of {1:.2f}".format("Cartman",skew(36, 31, 32, 33, 33)))
print("{0}'s running times have a skew of {1:.2f}".format("Kenny",skew(33, 32, 34, 31, 35)))
print("{0}'s running times have a skew of {1:.2f}".format("Bebe",skew(27, 29, 29, 28, 30)))
print()
maxMin("Stan", 34, 34, 35, 31, 29)
maxMin("Kyle", 30, 31, 29, 29, 28)
maxMin("Cartman", 36, 31, 32, 33, 33)
maxMin("Kenny", 33, 32, 34, 31, 35)
maxMin("Bebe", 27, 29, 29, 28, 30)