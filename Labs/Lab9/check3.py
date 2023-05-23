# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:24:32 2022

@author: jc219
"""

from Date import Date

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]


def find_month(list_birthday):
    date = []
    for j in list_birthday:
        s = j.strip().split('/')
        date.append(s)
        
    x = []
    y = []
    
    for k in date:
        x.append(k[1])
        x.sort()
    c1 = x.count("01")
    c2 = x.count("02")
    c3 = x.count("03")
    c4 = x.count("10")
    c5 = x.count("05")
    c6 = x.count("06")
    c7 = x.count("07")
    c8 = x.count("08")
    c9 = x.count("10")
    c10 = x.count("12")
    y.append(c1)
    y.append(c2)
    y.append(c3)
    y.append(c4)
    y.append(c5)
    y.append(c6)
    y.append(c7)
    y.append(c8)
    y.append(c9)
    y.append(c10)
    m = max(y)
    index = y.index(m)
    index += 1
    return index
    
list_birthday = []
for line in open('birthdays.txt', 'r'):
    split = line.strip().split()
    dates = Date(int(split[0]), int(split[1]), int(split[2]))
    dates = str(dates)
    list_birthday.append(dates)
   
list_birthday.sort()
    
earliest = list_birthday[0]
latest = list_birthday[-1]


print("Earliest =", earliest)
print("Latest =", latest)
print(month_names[find_month(list_birthday)])