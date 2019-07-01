import random, os, csv, sys

class scrabble:
    VOWELS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

    SLV = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
        'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
        'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
        'y': 4, 'z': 10, '*':0
    }


    ''' Change Directory '''
##    os.chdir("d:/")
    os.chdir("d:/Documents")
##    print(f"\n{os.getcwd()}")

    wordBucket = []
    steps = 0
    guesses = 3
    score = 0
    turn = 0
    tiles = ['*', '*', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e',
             'e', 'e', 'e', 'e', 'a', 'a', 'a', 'a', 'a', 'a',
             'a', 'a', 'a', 'i', 'i', 'i', 'i', 'i', 'i', 'i',
             'i', 'i', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
             'n', 'n', 'n', 'n', 'n', 'n', 'r', 'r', 'r', 'r',
             'r', 'r', 't', 't', 't', 't', 't', 't', 'l', 'l',
             'l', 'l', 's', 'u', 's', 'u', 's', 'u', 's', 'u',
             'd', 'd', 'd', 'd', 'g', 'g', 'g', 'b', 'c', 'm',
             'p', 'f', 'h', 'v', 'w', 'y', 'b', 'c', 'm', 'p',
             'f', 'h', 'v', 'w', 'y', 'k', 'j', 'x', 'q', 'z']


    def openFile():
        with open("sowpods.txt", "r") as oFile:
            rFile = csv.reader(oFile)

            for docLine in rFile:
                for docWord in docLine:
                    Words = docWord.split(" ",5)
                    for wordIndex in range(len(Words)):
                        if Words[wordIndex] != "":
                            scrabble.wordBucket.append(Words[wordIndex])
                        
        return print(f"{len(scrabble.wordBucket)} words have been loaded to the Bucket")
## End of OpenFile() method


    def calcPoints(words):
        # TODO:
        """
            Calculate a word that has "*" before replacing the asterisks
        """
        points = 0
        for letter in words.lower():
            if letter in scrabble.SLV.keys():
                points += scrabble.SLV[letter]
        points *= len(words)
        if len(words) == 7 and scrabble.turn == 1:
            points += 50
        scrabble.score += points
        return points
## End of CalculatePoints() function
## End of Scrabble class

scrabble.openFile()

retiles = scrabble.tiles
hand = []

def giveHand(handList):
    newList = handList
    if len(handList) >= 7:
        return handList
    elif len(retiles) <= 0:
        print("Game Over".upper())
        sys.exit()
    else:
        while len(newList) < 7 and len(retiles) >= 1:
            newtiles = []
            newtiles.append(retiles[random.randint(0,len(retiles)-1)].upper())
            newList += newtiles
            for letter in newtiles:
                retiles.remove(letter.lower())
        handList = newList
    return handList
## End of GiveHand function


def exchangeHand(someList, someHand):
    if len(someList) <= 7:
        return "You cannot exchange when there are 7 or less tiles in the bag"
    else:
        removeTiles = input("\nWhat letters do you want to exchange: ").upper()
        if len(removeTiles) <= 7:
            for letters in removeTiles:
                if letters in someHand:
                    someList += letters
                    someHand.remove(letters)
            retiles = someList
        print()
        return giveHand(someHand)
## End of Exchange function


def checkWord(someAnswer, someHand):
    # TODO:
    """
        see if word exist in wordbucket
        every letter used to answer be removed from hand        
    """
    global hand
    newList = []
    spareHand = []
    spareHand += someHand
    if "*" in someAnswer:
        wildWord = input("What letter replaces the '*'? ")
        newWord = someAnswer.replace("*",wildWord.upper())
        if newWord in scrabble.wordBucket:
            for letter in someAnswer:
                if letter in someHand:
                    hand.remove(letter)
            print(f"You scored {scrabble.calcPoints(someWord)} points.\n")
        else:
            print("\n Lol, That word does not exist in my vocabulary\n")
    elif someAnswer in scrabble.wordBucket:
        for letter in someAnswer:
            if letter in someHand:
                newList.append(letter)
            elif letter not in someHand:
                print(f"\n {letter} does not exist in the hand given to you.\n")
                return giveHand(someHand)
        for nletter in newList:
            if nletter in spareHand:
                spareHand.remove(nletter)
            else:
                print("\n Letters that appear once cannot be used twice\n")
                return giveHand(hand) 
        hand = spareHand
            
        print(f"\nYou scored {scrabble.calcPoints(someAnswer)} points\n")
        return giveHand(hand)

    else:
        print("\n Lol, That word does not exist in my vocabulary\n")
    return giveHand(hand)
## End of checkWord function

print("Type '.EX' to exchange tiles in your hand. .EX \n")
giveHand(hand)

while True:
    print(" ".join(hand).upper())
    Ans = input("Enter: ").upper()
    if Ans == ".EX":
        exchangeHand(retiles, hand)
    else:
        checkWord(Ans, hand)
