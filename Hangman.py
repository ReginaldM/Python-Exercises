import re, sys

sWord = ('tshimologo').upper()
secWord = list(sWord)
user = ['_' for i in secWord]
wrongWords = []

i = 7

while i != 0:
    wrongs = ", ".join(wrongWords)
    userWord = " ".join(user)
    
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
                    finalWord = " ".join(secWord)
                    print(f"\n{finalWord}\n\n{('Congratulations').upper()}")
                    sys.exit()
            else:
                if z not in wrongWords:
                    wrongWords.append(z)
                    i -= 1
                    if i <= 0:
                        print("You ran out of guesses")
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
