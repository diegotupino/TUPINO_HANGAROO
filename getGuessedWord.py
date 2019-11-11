def getGuessedWord(secretWord, lettersGuessed):
    temp = []
    word = ""
    for i in secretWord:
        if i in lettersGuessed:
            word += i
        else:
            word += "*"
    return word
    
                