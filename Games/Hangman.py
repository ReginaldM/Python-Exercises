import os, re, csv, sys, random

''' Change Directory '''
os.chdir("d:/documents")
print(f"\n{os.getcwd()}")

def openFile():
    with open("test.txt", "r") as rFile:
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
    wordBucketIndex = random.randint(0,len(wordBucket) - 1)
    wordFromIndex = wordBucket[wordBucketIndex].upper()

    global sWord
    sWord = wordFromIndex 
    return wordFromIndex
## End of generateWord() function

wordBucket = []
openFile()
generateWord()
user = ['_' for i in sWord]
wrongWords = []
tries = 7

while tries != 0:
    wrongs = ", ".join(wrongWords)
    userWord = " ".join(user)
    
    print(f"\nIncorrect words guessed: {wrongs} \
            \nGuess this word: \n\n{userWord}\n")
    answer = input(f"\nEnter your guess: ").upper()
    userLetter = list(answer)

    if answer.isalpha():        
        for letters in userLetter:
            if letters in sWord:
                letterIndexs = [m.start() for m in re.finditer(letters, sWord)]
                for indx in letterIndexs:
                    user[indx] = letters
                if user == list(sWord):  # userWord[::2] == sWord
                    print(f"\n{sWord}\n\n{('Congratulations').upper()}")
                    sys.exit()
            else:
                if letters not in wrongWords:
                    wrongWords.append(letters)
                    tries -= 1
                    if tries <= 0:
                        print(f"\n\nYou ran out of guesses. \
                            \nThe word was:   {sWord}")
                        sys.exit()
    else:
        print("Your input is not a valid Alphabet".upper())
        continue
