#import module from syllables file
from syllables import find_num_syllables

#Input statement that prompts user to enter a paragraph
paragraph = input("Enter a paragraph => ")
paragraph = paragraph.strip()
print(paragraph)

#Split is the function that makes every word into a string in a list
split = paragraph.split()

'''calculating ASL. Since periods indicate the end of a sentence, ASL total amount of words (len(split)) divided by the total number of periods'''
periods = paragraph.count('.')
ASL = len(split)/periods

'''
calculating PHW (Percent Hard words) and calculating LHW (List Hard words)
For every character in the splitted list the program isolates the words with greater than 3 syllables, has no dash, and does not end with es or ed
The words that meet the criteria are put in the list (words) and the count variable helps count the total number of hard words
To calculate the percentage we divide the number of hard words by the total amount of words-(len(split))
'''
count = 0
words = []
for char in split:
    if find_num_syllables(char) >= 3 and char.count('-') == 0 and char.endswith('es') == False and char.endswith('ed') == False:
        words.append(char)
        count += 1
PHW = (count/len(split))*100
words = str(words)

'''
Calculating ASYL (Average Num of Syllables)
I used another count variable count1 so that it doesn't interfere with the first count
This part of the program counts the number of syllables each word has and keeps adding it to count1
The program uses the for loop to go through every word
ASYL is found using count1 (total num of syllables) divided by total number of words
'''
count1 = 0
for word in split:
    count1 += find_num_syllables(word)
ASYL = count1/len(split)

print("Here are the hard words in this paragraph:\n" + words)
print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(ASL, PHW, ASYL))
print("Readability index (GFRI): {:.2f}".format(0.4*(ASL + PHW)))
print("Readability index (FKRI): {:.2f}".format(206.835-1.015*ASL-86.4*ASYL))

'''
given formulas:
GFRI = 0.4*(ASL + PHW)
FKRI = 206.835-1.015*ASL-86.4*ASYL
'''
