from ast import Or


infile = open('WorldSeriesWinners.txt','r')


dict = {}
dict2 = {}

display_year = int(input("Choose a year that you would like to show:"))


year = 1904


for display in infile:
    if display_year < 1904:
        print("Choose a number between 1904 and 2009")
    elif display_year > 2009:
        print("Choose a number between 1904 and 2009")
    else:
        for words in infile:
            #words.rstrip("\n")  
            #word.append(words.replace("\n", ""))
            dict2[year] = words
            year += 1

            if words in dict:
                dict[words] += 1
            else:
                dict[words] = 1

        

print(dict2[display_year], dict[dict2[display_year]])
    

