import random, os, csv, sys

class scrabble:

    ''' Change Directory '''
    os.chdir("d:/Documents")
    # print(f"\n{os.getcwd()}")

    # VOWELS = 'aeiou'
    # CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

    ScrabbleLetterValue = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
        'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
        'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
        'y': 4, 'z': 10, '*':0
    }

    wordBucket = []
    score = 0
    turn = 0
    hand = []

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
        '''Reads a text file and extract words into the wordBucket'''
        with open("sowpods.txt", "r") as oFile:
            rFile = csv.reader(oFile)

            for docLine in rFile:
                for docWord in docLine:
                    Words = docWord.split(" ",5)
                    for wordIndex in range(len(Words)):
                        if Words[wordIndex] != "":
                            scrabble.wordBucket.append(Words[wordIndex])
                        
        return print(f"{len(scrabble.wordBucket)} words have been loaded...")
    ## End of OpenFile() method


    def calcPoints(word):
        '''Calculate points for a given word'''
        points = 0
        for letter in word.lower():
            points += scrabble.ScrabbleLetterValue.get(letter,0)
        points *= len(word)
        if len(word) == 7 and scrabble.turn == 1:
            points += 50
        scrabble.score += points
        return points
    ## End of CalculatePoints() function

    def giveHand(handList):
        '''Deals 7 tiles to a player.'''
        newList = []
        newList += handList
        if len(handList) >= 7:
            return handList
        elif len(scrabble.tiles) <= 0:
            print("Game Over".upper())
            sys.exit()
        else:
            while len(newList) < 7 and len(scrabble.tiles) >= 1:
                newtiles = []
                newtiles.append(scrabble.tiles[random.randint(0,len(scrabble.tiles)-1)].upper())
                newList += newtiles
                for letter in newtiles:
                    scrabble.tiles.remove(letter.lower())
            scrabble.hand = newList
        return scrabble.hand
    ## End of GiveHand function


    def exchangeHand(tilesBag, someHand):
        '''
            Exhanges given tiles for new ones in the tile bag so long
            there are more than 7 tiles in the bag
        '''
        if len(tilesBag) <= 7:
            return "You cannot exchange tiles when there are 7 or less tiles in the bag \n"
        else:
            removeTiles = input("\nWhich letters do you want to exchange: ").upper()
            if len(removeTiles) <= 7:
                for letters in removeTiles:
                    if letters in someHand:
                        tilesBag += letters
                        someHand.remove(letters)
                scrabble.tiles = tilesBag
            scrabble.hand = someHand
            return scrabble.giveHand(someHand)
    ## End of Exchange function


    def verifyWord(someAnswer, someHand):
        '''Verifies that the letters used to form a word are from the given hand'''
        newList = []
        spareHand = []
        spareHand += someHand
        for letter in someAnswer:
            if letter in someHand:
                newList.append(letter)
            elif letter not in someHand:
                print(f"\n {letter} does not exist in the hand given to you.\n")
                return scrabble.giveHand(someHand)
        for nletter in newList:
            if nletter in spareHand:
                spareHand.remove(nletter)
            else:
                print("\n Letters that appear once in hand cannot be used twice\n")
                return scrabble.giveHand(someHand)
        scrabble.hand = spareHand
        print(f"\nYou scored {scrabble.calcPoints(someAnswer)} points\n")
        return scrabble.giveHand(scrabble.hand)
    # End of VerifyWord function


    def checkWord(someAnswer, someHand):
        '''Verifies if given word exist in wordbucket'''
        nonExistent = "\n Lol, That word does not exist in my vocabulary\n"
        if "*" in someAnswer:
            wildWord = input("Which letter should replace the '*'? ")
            newWord = someAnswer.replace("*",wildWord.upper())
            if newWord in scrabble.wordBucket:
                scrabble.verifyWord(someAnswer, scrabble.hand)
            else:
                print(nonExistent)
        elif someAnswer in scrabble.wordBucket:
            scrabble.verifyWord(someAnswer, scrabble.hand)
        else:
            print(nonExistent)
        return scrabble.giveHand(someHand)
    ## End of checkWord function
## End of Scrabble class

scrabble.openFile()
print("\n Type '.EX' to exchange tiles in your hand. .EX \n")
scrabble.giveHand(scrabble.hand)

while True:
    print(" ".join(scrabble.hand).upper())
    Ans = input("Enter: ").upper()
    if Ans == ".EX":
        scrabble.exchangeHand(scrabble.tiles, scrabble.hand)
    else:
        scrabble.checkWord(Ans, scrabble.hand)
