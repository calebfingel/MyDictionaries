infile = open('Al.txt','r')

dict = {}
#words =str.split()

#counter = 0
for words in infile:
    if words not in dict:
        dict[words] = 0
    dict[words] += 1

print(dict)
    
