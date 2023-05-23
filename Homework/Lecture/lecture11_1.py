# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:23:06 2022

@author: jc219
"""

'''
The function first compares the year and returns false if w1 is greater
then it finds that if both values are in the spring and the same year they are not equal
lastly the function finds when spring is > fall and returns true. All other returns false
'''

def earlier_semester(w1, w2):
    if w2[1] >= w1[1]:
        if w1[0] == 'Spring' and w2[0] == 'Spring':
            return False
        elif w1[0] == 'Spring' or w2[0] == 'Fall':
            return True
    return False
w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w1,w3)))