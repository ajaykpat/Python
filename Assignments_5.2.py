#!/usr/bin/python3
# Assignment:5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
#and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

smallest = None
largest = None

while True :
    x = input (' Enter number:')
    if x == 'done' :
        break
    else :
        try :
            x= int (x)
        except :
            print ('Invalid input')
            continue
        if smallest is None :
            smallest = x
        elif x < smallest :
            smallest = x
        if largest is None :
            largest = x
        elif x > largest :
                largest =x
    continue

print ('Minimum is',smallest)
print ('Maximum is',largest)
