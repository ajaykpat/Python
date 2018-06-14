#! /usr/bin/python3
# Assignment : 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
# Written by : ajaykpat

grade = input ('Enter the Grade between 0.0 and 1.0:')
try:
    floatgrade = float(grade)
except:
    print ('Enter an acceptable value')
    quit()
if floatgrade > 1 :
    print ('Grade value out of range. Please re-enter Correct value')

elif floatgrade >= 0.9 :
    print ('A')
elif floatgrade >= 0.8 :
    print ('B')
elif floatgrade >= 0.7 :
    print ('C')
elif floatgrade >= 0.6 :
    print ('D')
elif floatgrade < 0.6 :
    print ('F')
