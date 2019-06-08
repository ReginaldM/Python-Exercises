import random

"""
Player enters a 4-digit secret number. The digits must be all different.
The player tries to guess the numberthat matches.
If the matching digits are in their right positions, they are "bulls",
if in different positions, they are "cows"
"""

secretNum = []

def genNum():
    for i in range(9):
        ranNum = str(random.randint(0,9))
        if len(secretNum) == 4:
            break
        elif ranNum in secretNum:
            pass
        else:
            secretNum.append(ranNum)


def findBullCow(secretDigit):
    while True:
        bull = 0
        cow = 0

        playerResponse = input("Enter: ")
        
        if playerResponse == 'exit':
            break
        elif secretDigit == list(playerResponse):
            print(f"\nCongratulations on getting 4 bulls\n")
            print(f" secretDigit: {secretDigit}\n playerResponse: {list(playerResponse)}\n")
            break
        else:
            for x,y in zip(secretDigit,list(playerResponse)):
                if x == y:
                    bull += 1
                else:        
                    for y in list(playerResponse):
                        if y == x:
                            cow += 1
                        else:
                            pass
        print(f"bulls = {bull}, cows = {cow}\n")

genNum()
findBullCow(secretNum)
