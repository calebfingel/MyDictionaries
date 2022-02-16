import re

infile = open('AI.txt','r')


dict = {}

count = 0
for words in infile:
    clean_word = re.sub("[^A-Za-z0-9 ]+", "",words)
    words_split = clean_word.split()

    for text in words_split:
        if text in dict:
            dict[text] += 1
        else:
            dict[text] = 1

print(dict)
    
