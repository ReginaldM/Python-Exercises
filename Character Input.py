import datetime

currentDate = datetime.date.today().strftime("%Y")

userName = input("Enter your Name: ")
userAge = int(input('Please enter your age: '))
numTimes = int(input("Enter any number: "))

predictYear = 100 - userAge


print(numTimes*f"\nDid you know {userName}, that you will turn a 100 years old in the year {int(currentDate) + predictYear}")

