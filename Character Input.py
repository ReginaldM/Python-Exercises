import datetime
"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them
the year that they will turn 100 years old.
"""


currentDate = datetime.datetime.now()

userName = input("Enter your Name: ")
userAge = int(input('Please enter your age: '))
numTimes = int(input("Enter any number: "))
predictYear = 100 - userAge


print(numTimes*f"\nDid you know {userName}, that you will turn a 100 years old in the year {int(currentDate.year) + predictYear}")

