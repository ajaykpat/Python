#! /usr/bin/python3
#Assignment :7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt
#Written By : ajaykpat

filename = input ('Enter the file name:')

readfile = open (filename)

x = readfile.read()

x= x.rstrip()

x = x.upper()

print (x)
