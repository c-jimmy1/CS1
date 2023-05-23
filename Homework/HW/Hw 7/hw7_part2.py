# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 01:12:11 2022

@author: jc219

HW 7 Part 2 is finding the best and worst movies between given years. 
The program will keep running until stop is entered.
"""
import json

'''lowercasing the genres in the dictionary by creating a new lowered list and resetting it equal to'''
def lowercase(movieID, movies): 
    temp = []
    for name in movies[movieID]['genre']:
        name = name.lower()
        temp.append(name)
        movies[movieID]['genre'] = temp

    
if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

'''defining values using inputs'''
min_year = input('Min year => ').strip()
print(min_year)
min_year = int(min_year)

max_year = input('Max year => ').strip()
print(max_year)
max_year = int(max_year)

w1 = input('Weight for IMDB => ').strip()
print(w1)
w1 = float(w1)

w2 = input('Weight for Twitter => ').strip()
print(w2)
w2 = float(w2)

id_and_rating = dict() # id_and_rating contains the movieID and rating where rating is the value

for movieID in movies: # for every movieID in the dictionary of movies
    year = int(movies[movieID]['movie_year'])
    imdb_rating = movies[movieID]['rating']
    lowercase(movieID, movies)

    if movieID in ratings and len(ratings[movieID]) >= 3: # filtering out the movies that dont have any ratings or if there are less than 3 ratings
        listratings = ratings[movieID]
        average_twitter_rating = sum(listratings)/len(listratings) # calculating the average twitter ratings
        if year >= min_year and year <= max_year: # filtering for the years chosen
            combined_rating = (w1 * imdb_rating + w2 * average_twitter_rating) / (w1 + w2) 
            id_and_rating[movieID] = combined_rating # {movieID: rating calculation}
    else:
        pass

stop = False # defining stop outside of loop
while True: # infinitely runs loop until a break statement is used
    genre = input('\nWhat genre do you want to see? ').strip()
    print(genre)
    genrelower = genre.lower()
    if genrelower == 'stop': # if the input is stop, break the loop and not print anything
        stop == True
        break
    
    sortedvalues = [] # initialize empty list
    for movieID2, rating in id_and_rating.items(): # for movieID2, rating in the dictionary
        if genrelower in movies[movieID2]['genre']: # if the genre inputted is in the list of genres
            tuples = (rating, movieID2) # create a tuple with the ratings first
            sortedvalues.append(tuples) # append all tuples to the list sorted values

    if len(sortedvalues) == 0: # if the length of sortedvalues is 0 then there are no movies with the genre inputed
        found = False # set found equal to false
    else:
        sortedvalues.sort(reverse = True) # sort the list from greatest to least
        largest = sortedvalues[0][1] # the largest is the first value
        smallest = sortedvalues[-1][1] # the smallest is the last value
        found = True # set found equal to ture
    
    if not stop: # if not stop keep going
        if found: # if found is True print best and worst
            print('\nBest:')
            print('        Released in {}, {} has a rating of {:.2f}'.format(movies[largest]['movie_year'], movies[largest]['name'], sortedvalues[0][0]))
            print('\nWorst:')
            print('        Released in {}, {} has a rating of {:.2f}'.format(movies[smallest]['movie_year'], movies[smallest]['name'], sortedvalues[-1][0]))
        else: # if found is False print not found
            print('\nNo {} movie found in {} through {}'.format(genre.title(), min_year, max_year))
    else: # else break the loop
        break
       