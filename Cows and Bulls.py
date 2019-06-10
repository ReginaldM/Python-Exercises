import random

"""
Player enters a 4-digit secret number. The digits must be all different.
The player tries to guess the numberthat matches.
If the matching digits are in their right positions, they are "bulls",
if in different positions, they are "cows"
"""

secretNum = []

def genNum():
    for iSteps in range(9):
        ranNum = str(random.randint(0,9))
        if len(secretNum) == 4:
            break
        elif ranNum in secretNum:
            pass
        else:
            secretNum.append(ranNum)
## End of genNum method

def findBullCow(secretDigit):
    genNum()
    print("Type the word 'exit' to quit the program")
    while True:
        bull = 0
        cow = 0
        playerResponse = input("Enter: ")

        if playerResponse == 'exit':
            break
        elif secretDigit == list(playerResponse):
            sD = "".join(secretDigit)
            print(f"\nCongratulations! 4 bulls acquired \
                \nSecret Number: {sD}\n Player Number: {playerResponse}\n")
            break
        else:
            for x,y in zip(secretDigit,list(playerResponse)):
                if x == y:
                    bull += 1
                elif y in secretDigit:
                    cow += 1

        print(f"bulls = {bull}, cows = {cow}\n")
## End of findBullCow method


findBullCow(secretNum)
