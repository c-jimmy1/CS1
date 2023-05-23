# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:32:21 2022

@author: jc219

This program outputs information regarding COVID. It helps find states with significant spread of the virus.
It's needed to determine which communities must self quarantine
"""
import hw4_util

#calculates the daily average of each state in quar function
def daily2(state):    
    avg = ((state[2] + state[3] + state[4] + state[5] + state[6] + state[7] + state[8])/state[1])/7
    daily_avg = avg*100000
    return daily_avg

#calculates the pct of each state in quar function
def pct2(state):

    total_cases = (state[2] + state[3] + state[4] + state[5] + state[6] + state[7] + state[8]) + (state[9] + state[10] + state[11] + state[12] + state[13] + state[14] + state[15])
    pct = ((state[2] + state[3] + state[4] + state[5] + state[6] + state[7] + state[8]) / total_cases) * 100
    return pct

#uses the daily2 and pct2 function to determine the states that are quarantined
def quar(week_picked):
    quar_list = []
    for x in week_picked:
        if daily2(x) >= 10 or pct2(x) >= 10: # checks that daily avg is > 10 and daily pos percent > 10
            quar_list.append(x[0]) #adds all the states that meet the criteria (index 0 of x)
    return hw4_util.print_abbreviations(quar_list)

#uses the daily2 function to find the highest rate and print the state that has the highest rate
def high(week_picked):
    avg_states = []
    for x in week_picked:
        avg_states.append(daily2(x)) #adds avg for every state in the week to a list
    highest = max(avg_states) # finds the largest avg of the list
    
    for x in week_picked:
        if highest == daily2(x): #tests the largest avg in all avgs
            index = x[0] #finds the index of the highest
    return highest, index

found_state = False

i = 0
while i != -1: #makes sure that when a negative is entered the program stops
    print('...')
    week = int(input('Please enter the index for a week: '))
    print(week)
    
    totalweek = 29
    if week > totalweek:
        print('No data for that week')
    else:    
        if week <= 0:
            i = week
            break
        
        elif week > 0:
            request = input('Request (daily, pct, quar, high): ')
            request = request.strip()
            print(request)
            request = request.lower()
            
            week_picked = hw4_util.part2_get_week(week)

            if request == 'daily':
                state = input('Enter the state: ')
                state = state.strip()
                print(state)
                
                found_state = False
                
                for z in week_picked: 
                    if z[0] == state:
                        found_state = True
                            
                if found_state == True: #if the state is found in the list the program moves on
                    for x in range(len(week_picked)):
                        
                        #The below finds the avg daily positive (adding all the positive and dividing by 7)
                        if week_picked[x][0] == state:
                            index = x
                            avg = ((week_picked[index][2] + week_picked[index][3] + week_picked[index][4] + week_picked[index][5] + week_picked[index][6] + week_picked[index][7] + week_picked[index][8])/week_picked[index][1])/7
                    #multiplies avg by 100000 so we get it per 100k ppl
                    daily_avg = avg*100000 
                    print('Average daily positives per 100K population: {:.1f}'.format(daily_avg))
                else:
                    print("State {} not found".format(state))  


            elif request == 'pct':
                state = input('Enter the state: ')
                state = state.strip()
                print(state)
                
                found_state = False
                
                for z in week_picked:
                    if z[0] == state:
                        found_state = True
                
                if found_state == True: #if the state is found in the list the program moves on
                    for x in range(len(week_picked)):
                        
                        #The below program adds the positive cases and negative cases to get the total cases
                        if week_picked[x][0] == state:
                            index = x
                            total_cases = (week_picked[index][2] + week_picked[index][3] + week_picked[index][4] + week_picked[index][5] + week_picked[index][6] + week_picked[index][7] + week_picked[index][8]) + (week_picked[index][9] + week_picked[index][10] + week_picked[index][11] + week_picked[index][12] + week_picked[index][13] + week_picked[index][14] + week_picked[index][15])
                    
                    #total positive cases/ total overall cases is PCT
                    pct = ((week_picked[index][2] + week_picked[index][3] + week_picked[index][4] + week_picked[index][5] + week_picked[index][6] + week_picked[index][7] + week_picked[index][8]) / total_cases) * 100
                    print('Average daily positive percent: {:.1f}'.format(pct))
                else:
                    print("State {} not found".format(state))    
            elif request == 'quar':
                print('Quarantine states:')
                quar(week_picked)
                
            elif request == 'high':
                print('State with highest infection rate is {}'.format(high(week_picked)[1]))
                print('Rate is {:.1f} per 100,000 people'.format(high(week_picked)[0]))
            
            else:
                print('Unrecognized request')
