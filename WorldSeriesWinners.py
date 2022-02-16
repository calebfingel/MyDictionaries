from ast import Or


infile = open('WorldSeriesWinners.txt','r')


dict = {}
dict2 = {}

display_year = int(input("Choose a year that you would like to show:"))


year = 1904


for display in infile:
    if display_year < 1904:
        print("Choose a number between 1904 and 2009")
        display_year = int(input("Choose a year that you would like to show:"))
    elif display_year > 2009:
        print("Choose a number between 1904 and 2009")
        display_year = int(input("Choose a year that you would like to show:"))
    else:
        for words in infile:
            dict2[year] = words
            year += 1

            if words in dict:
                dict[words] += 1
            else:
                dict[words] = 1

        

print(dict2[display_year], dict[dict2[display_year]])
    

