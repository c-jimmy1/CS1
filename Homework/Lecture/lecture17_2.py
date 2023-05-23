# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:44:17 2022

@author: jc219
"""

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    
    if movie in movies:
        movies[movie].add(name)
    else:
        movies[movie] = set()
        movies[movie].add(name)

singlets = 0
most = 0

for movie in movies:
    name_ct = len(movies[movie])
    
    if name_ct == 1:
        singlets += 1
    if name_ct > most:
        most = name_ct
        movie1 = movie
print(most)
print(movie1)
print(singlets)        
