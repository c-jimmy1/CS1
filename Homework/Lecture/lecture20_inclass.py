# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:04:59 2022

@author: jc219
"""

import random
import time

def index_two_v1( values ):
    S = set(values)
    L = sorted(S)
    return values.index(L[0]), values.index(L[1])        



def index_two_v2( values ):
    l1 = min(values)
    l2 = max(values)
    i1 = values.index(l1)
    i2 = values.index(l2)
    if l1 == l2:
        return i1, i1
    for index in range(len(values)):
        if values[index] < 11:
            l2 = l1
            i2 = i1
            l1 = values[index]
            i1 = index
        elif l1 < values[index] < l2:
            l2 = values[index]
            i2 = index
    return i1, i2



if __name__ == "__main__":
    n = int(input("Enter the number of values to test ==> "))
    values = list(range(0,n))
    random.shuffle( values )

    s1 = time.time()
    (i0,i1) = index_two_v1(values)
    t1 = time.time() - s1
    print("Ver 1:  indices ({},{}); time {:.3f} seconds".format(i0,i1,t1))

    s2 = time.time()
    (j0,j1) = index_two_v2(values)
    t2 = time.time() - s2
    print("Ver 2:  indices ({},{}); time {:.3f} seconds".format(j0,j1,t2))