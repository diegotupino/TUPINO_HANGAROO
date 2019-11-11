def getAvailableLetters(lettersGuessed):
    word = ""
    count = 0
    characters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in characters:
        if letter in lettersGuessed:
            count += 1
        else:
                word += letter
    return word