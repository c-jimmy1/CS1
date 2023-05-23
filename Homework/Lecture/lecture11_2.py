# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:19:22 2022

@author: jc219
"""

hd = int(input("Enter Dale's height: "))
print(hd)

he = int(input("Enter Erin's height: "))
print(he)

hs = int(input("Enter Sam's height: "))
print(hs)

#tests for each case and prints the names from greatest to least
if hd > he and hd > hs and he > hs:
    print("Dale\nErin\nSam")
elif hd > he and hd > hs and hs > he:
    print("Dale\nSam\nErin")
elif he > hd and he > hs and hd > hs:
    print("Erin\nDale\nSam")
elif he > hd and he > hs and hs > hd:
    print("Erin\nSam\nDale")
elif hs > hd and hs > he and he > hd:
    print("Sam\nErin\nDale")
elif hs > hd and hs > he and hd > he:
    print( "Sam\nDale\nErin")

