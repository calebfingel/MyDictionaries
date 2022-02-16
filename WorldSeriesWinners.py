infile = open('WorldSeriesWinners.txt','r')

dict_number_times = {}

for words in infile:
    #if words not in dict_number_times:
        #dict_number_times[words] = 0
    dict_number_times[words] += 1

print(dict_number_times)


dict_years = {}
counter = 1902
    for years in infile:
        counter += 1
        
