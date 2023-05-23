# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:08:31 2022

@author: jc219
"""
import random
import time


def addone(x):

    return x+1

def closest1(lists):

    if len(lists) < 2:
        return None, None
    variable = 10000000
    x1 = 0
    x2 = 0
    for x in lists:
        for y in lists:
            if x == y:
                continue
            difference = abs(x - y)
            if difference < variable:
                variable = difference
                x1 = x
                x2 = y
                
    return x1, x2

def closest2(lists):
    '''
    >>> closest2([])
    (None, None)
    >>> closest2([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (4.3, 5.4)
    >>> closest2([2, 2, 3, 3])
    (2, 2)
    >>> closest2([-1.3, 1.7, -9.2])
    (-1.3, 1.7)
    '''
    
    if len(lists) < 2:
        return None, None
    variable = 10000000
    x1 = 0
    x2 = 0
    listcopy = lists.copy()
    listcopy = sorted(listcopy)
    for x in range(len(listcopy)-1):
        first = listcopy[x]
        second = listcopy[x+1]
        difference = abs(first - second)
        if difference < variable:
            variable = difference
            x1 = first
            x2 = second
            
    return x1, x2
L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]


if __name__ == "__main__":
    randomList = []
    for x in range(10000):
        randomList.append(random.uniform(0.0, 1000.0))
    s1 = time.time()
    (i0,i1) = closest1(randomList)
    t1 = time.time() - s1
    print('time for first one:', t1)

    s2 = time.time()
    (j0,j1) = closest2(randomList)
    t2 = time.time() - s2
    print('time for second one:', t2)
