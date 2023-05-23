# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:15:28 2022

@author: jc219
"""

def parse_line(text):
    x = text.split('/')
    nums = x[-3:]
    del x[-3:]
    nums = (' '.join(map(str, nums)))
    nums = nums.split(' ')
    check = ''.join(map(str, nums))
    x = ('/'.join(x))
    if check.isdigit():
        x1 = (int(nums[0]), int(nums[1]), int(nums[2]), x)
        print(x1)
    else:
        return None

print(parse_line("Here is some random text, like 5/4=3./12/3/4"))

print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))

print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))

print(parse_line(" Here is some spaces 12/32/4"))

print(parse_line(" Again some spaces\n/12/12/12"))