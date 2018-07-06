#! /usr/bin/python3
# Assignment : 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# written by : ajaykpat

x = input (' Open the file name :')

y = open (x)
finalli = []
for i in y :
    i = i.rstrip()
    words = i.split()
    for b in words:
        if not b in finalli :
            finalli.append(b)
#        else:
#           pass

finalli.sort()
print (finalli)
