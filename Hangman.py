import re, sys, os, csv, random

''' Change Directory '''
os.chdir("d:/documents")
print(f"\n{os.getcwd()}")

def openFile():
    with open("sowpods.txt", "r") as rFile:
        oFile = csv.reader(rFile)

        for docLine in oFile:
            for docWord in docLine:
                wordList = docWord.split(" ")
                for wordStrings in wordList:
                    if wordStrings != "":
                        wordBucket.append(wordStrings)
            
    return f"WordBucket has been populated with {len(wordBucket)} words."
## End of OpenFile() method

def generateWord():
    ## a variable that'll represent a word in Array
    wordBucketIndex = random.randint(0,len(wordBucket))

    try:
        wordFromIndex = wordBucket[wordBucketIndex].upper()
    except IndexError as listIndexError:
        wordFromIndex = wordBucket[wordBucketIndex-1].upper()
        # outputErr = input("print Error Y/N: ").upper()
        # if outputErr == "Y":
            # print(f"\n{listIndexError}\n")

    global sWord
    sWord = wordFromIndex 
    return wordFromIndex
## End of generateWord() function

wordBucket = []
openFile()
generateWord()
secWord = list(sWord)
user = ['_' for i in secWord]
wrongWords = []
tries = 7

while tries != 0:
    wrongs = ", ".join(wrongWords)
    userWord = " ".join(user)
    finalWord = " ".join(secWord)
    
    print(f"Incorrect words guessed: {wrongs} \
            \nGuess this word: \n\n{userWord}\n")
    answer = input(f"\nEnter your guess: ").upper()
    userLetter = list(answer)

    if True:
        for z in userLetter:
            if z in secWord:
                wordIndexs = [m.start() for m in re.finditer(z, sWord)]
                for item in wordIndexs:
                    user[item] = z
                if user == secWord:
                    print(f"\n{finalWord}\n\n{('Congratulations').upper()}")
                    sys.exit()
            else:
                if z not in wrongWords:
                    wrongWords.append(z)
                    tries -= 1
                    if tries <= 0:
                        print(f"The word was {finalWord} \nYou ran out of guesses")
                        sys.exit()



##while i != 0:
##    wrongs = ", ".join(wrongWords)
##    userWord = " ".join(user)
##    
##    print(f"Incorrect words guessed: {wrongs} \
##            \nGuess this word: \n\n{userWord}\n")
##    userLetter = input(f"\n{i} Enter: ")
##
##    if userLetter == sWord or user == secWord:
##        print("\n{userWord}\nCongratulations")
##        break
##    elif userLetter in secWord:
##        wordIndexs = [m.start() for m in re.finditer(userLetter, sWord)]
##        for item in wordIndexs:
##            user[item] = userLetter
##        if user == secWord:
##            print(f"\n{userWord}\nCongratulations")
##            break
##    else:
##        wrongWords.append(userLetter)
##        i -= 1
