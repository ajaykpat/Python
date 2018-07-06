#! /usr/bin/python3
# Assignment 7.2 : Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# written By : ajaykpat


x = input ( ' Ener the file name :')

y = open (x)
count = 0
total = 0
for i  in y :

    if i.startswith('X-DSPAM-Confidence') :
        count = count +1

        value = i[20:26]

        value =value.strip()
        value = float(value)
        total = total + value


Avg = total / count

print ('Average spam confidence:', Avg)
