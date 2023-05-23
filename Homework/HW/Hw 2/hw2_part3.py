#determining the frequency a keyword is said using functions

def number_happy(sentence):
    sentence = sentence.lower()
    freq = sentence.count('laugh')
    freq += sentence.count('happiness')
    freq += sentence.count('love')
    freq += sentence.count('excellent')
    freq += sentence.count('good')
    freq += sentence.count('smile')
    return freq

def number_sad(sentence):
    sentence = sentence.lower()
    freq = sentence.count('bad')
    freq += sentence.count('sad')
    freq += sentence.count('terrible')
    freq += sentence.count('horrible')
    freq += sentence.count('problem')
    freq += sentence.count('hate')
    return freq

#User inputs a sentence
input_sentence = input('Enter a sentence => ')
input_sentence = input_sentence.strip()
print(input_sentence)

#uses the function to count the freq of the input
freq_happy = number_happy(input_sentence)
freq_sad = number_sad(input_sentence)

#changes the number into + and - signs
happyplus = freq_happy * '+'
sadminus = freq_sad * '-'
print("Sentiment:", happyplus + sadminus)

#using if else statements to compare the freq of sad and happy. if its equal the program prints the else statement
if freq_happy > freq_sad:
    print('This is a happy sentence.')
elif freq_happy < freq_sad:
    print('This is a sad sentence.')
elif freq_happy == freq_sad:
    print('This is a neutral sentence.')