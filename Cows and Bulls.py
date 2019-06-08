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

##    for x,y in zip(num,axs):
##        if x is y:
##            bull += 1
##        else:        
##            for y in axs:
##                if y is x:
##                    cow += 1
##                else:
##                    pass
##    return print(f"bulls = {bull}, cows = {cow}\n")











"""
while True:
    axs = input("Enter: ")
    if axs == 'exi':
        break
    elif num == list(axs):
        print(f"Congrats \nbulls = 4\n")
        break
    else:
        findBullCow()

print(f"\nx in num: {num}\ny in axs: {axs}\n")

for x,y in zip(num,axs):
##    print(f"x: {x}\n\nx={x} y={y}\n")
    if x is y:
        bull += 1
    else:        
        for y in axs:
            if y is x:
##                print(f"\nTheory working: y is {y}\n")
                cow += 1
            else:
                pass
##                print(f"Not working, y {y} is not {x}")

"""





##for x,y in zip(num,list(axs)):
##    [kn.append(x) for x in num if x is y]
##    [kn.append(x) if x is y else kn.append('') for x in num]
##    print(f"{x}, {[kn.append(x) for x in num if x is y]}")

##for x,y in zip(num,list(axs)):
##    if x is y:
##        kn.append(x)
##    else:
##        kn.append('')

##for i in range(len(kn)):
##    if num[i] is kn[i]:
##        bull += 1
##    else:
##        cow += 1
##
##print(f"Bulls: {bull}, Cows: {cow}")
