def hangaroo(secretWord):
    print("Hangarooo!")
    length = len(secretWord)
    print("The word has", length,"letters. ")
    chances = 5
    i = 0
    lettersGuessed = []
    while (chances!= 0):
        if secretWord != getGuessedWord(secretWord, lettersGuessed):
            print(chances, "guesses left. ")
            print("Available Letters: ", getAvailableLetters(lettersGuessed))
            guess = input("Type letter: ")
            guessInLowerCase = guess.lower()
            if guessInLowerCase in lettersGuessed:
                print("You already guessed this letter. Try again! ", getGuessedWord(secretWord, lettersGuessed))
            elif guessInLowerCase not in secretWord:
                print("Incorrect guess. Try again! ", getGuessedWord(secretWord, lettersGuessed))
                chances -= 1
            else:
                lettersGuessed.append(guessInLowerCase)
                print("You found a correct letter! ", getGuessedWord(secretWord, lettersGuessed))
        elif secretWord == getGuessedWord(secretWord, lettersGuessed):
                print("You guessed it right! ")
                break
    else:
        print("No guesses left. The word is " + secretWord)