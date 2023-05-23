# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:33:19 2022

@author: jc219
"""

def recursive_add( L ):

    return recursive_add_impl(L, 0)

def recursive_add_impl( L, i):
    '''
    The actual recursive function.
    '''
    if i == len(L)-1:
        return L[i]
    elif len(L)==0:
        return 0
    else:
        return L[i] + recursive_add_impl(L, i+1)


if __name__ == "__main__":
    L1 = [ 5 ]
    print(recursive_add(L1))
    L2 = [ 24, 23.1, 12, 15, 1 ]
    print(recursive_add(L2))
    print(recursive_add([ ]))

