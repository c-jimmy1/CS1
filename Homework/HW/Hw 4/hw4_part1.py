# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 22:13:58 2022

@author: jc219
"""
import hw4_util

#if the length is less than 6 the score is 0, if the length is 6 or 7 the score is 1, etc... this is tested using if else statements
def length_calc(password, score):
    length = len(password)
    if length < 6:
        score = 0
    elif length == 6 or length == 7:
        score += 1
        print('Length: +1')
    elif length == 8 or length == 9 or length == 10:
        score += 2
        print('Length: +2')
    else:
        score += 3
        print('Length: +3')
    return score
        
'''
counts for the number of uppercase letters and the amount of lowercase letters
if they are both greater than or equal to 2 they get 2 points, and if they are both at least 1, they get 1 point
'''
def case_calc(password, score):
    upper = 0
    lower = 0
    
    for character in password:
        if character.isupper():
            upper += 1
        
    for character in password: 
        if character.islower():
            lower += 1
            
    if upper >= 2 and lower >= 2:
        score += 2
        print('Cases: +2')
    elif upper >= 1 and lower >= 1:
        score += 1
        print('Cases: +1')
    else:
        score = 0
        
    return score

#checks for the total amount of digits using isnumeric(), then using if statments test the amount of points the user is rewarded
def digit_calc(password, score):
    digits = 0
    for character in password:
        if character.isnumeric():
            digits += 1
            
    if digits <= 0:
        score = 0        
    elif digits >= 2:
        score += 2
        print('Digits: +2')
    elif digits < 2:
        score += 1
        print('Digits: +1')
    return score

#counts the number of special characters, anything over 0 is 1 point
def punct_calc(password, score):
    score = 0
    if password.count('!') > 0:
        score = 1
        print('!@#$: +1')
    elif password.count('@') > 0:
        score = 1
        print('!@#$: +1')
    elif password.count('#') > 0:
        score = 1
        print('!@#$: +1')
    elif password.count('$') > 0:
        score = 1
        print('!@#$: +1')
    else:
        pass
    return score

#counts the number of special characters, anything over 0 is 1 point
#in a different function for readability and different print statment
def punct_calc2(password, score):
    score = 0
    if password.count('%') > 0:
        score = 1
        print('%^&*: +1')
    elif password.count('^') > 0:
        score = 1
        print('%^&*: +1')
    elif password.count('&') > 0:
        score = 1
        print('%^&*: +1')
    elif password.count('*') > 0:
        score = 1
        print('%^&*: +1')
    else:
        pass
    return score

'''
First checks if the length is equal to 7 bc license plates are 7 digits
next if statement checks if the first 3 characters are letters
last if statement checks if the last 4 characters are digits
if all criteria is met, the score is deducted by 2, otherwise there is no change in the score
'''
def license_check(password, score):
    if len(password) == 7:
        if password[0].isalpha() and password[1].isalpha() and password[2].isalpha():
            if password[3].isdigit() and password[4].isdigit() and password[5].isdigit() and password[6].isdigit():
                score = score - 2
                print("License: -2")
        else:
            score = 0
    return score

'''
convert all password to lower to compare
if the password is in top100 (the list from the other file)
Then score is subtracted by 3, otherwise score is not affected
'''
def common_pass(password, score):
    password = password.lower()
    top100 = hw4_util.part1_get_top()
    if password in top100:
        score = score - 3
        print("Common: -3")
    return score
        
password = input("Enter a password => ")
password = password.strip()
print(password)

score = 0

#adding all the different scores together from each function. The sum of them all is equal to the combined score.
combined = int(length_calc(password, score)) + int(case_calc(password, score)) + int(digit_calc(password, score)) + int(punct_calc(password, score)) + int(punct_calc2(password, score)) + int(license_check(password, score)) + int(common_pass(password, score))

print("Combined score:", combined)

#prints the strength of the password based on the rules given in the HW
if combined <= 0:
    print('Password is rejected')
elif combined == 1 or combined == 2:
    print('Password is poor')
elif combined == 3 or combined == 4:
    print('Password is fair')
elif combined == 5 or combined == 6:
    print('Password is good')
elif combined >= 7:
    print('Password is excellent')