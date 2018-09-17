from tkinter import *
from os import system
from random import randrange

root = Tk()
words = []
images = []
dashes = []
guessed = []
secretWord = 'Secret Word: '
guessedLetters = 'Guessed Letters: '
errors = 0
goal = ''

for word in open('words.txt'):
    words.append(word.rstrip())

images = open('images.txt').read()
images = images.split(',')

def startGame():
    global goal, correct
    goal = words[randrange(len(words))]
    numberOfLetters = correct = len(goal)
    for letter in goal:
        dashes.append('_ ')
    return(goal)

def TkGUI(position):
    global inputField, variableString, welcomeMessage, inputField, submitButton, secretWord, guessedLetters
    variableString = StringVar()
    for dash in dashes:
        secretWord = secretWord + dash
    for letter in guessed:
        guessedLetters = guessedLetters + letter + ' '
    #Due to TKinter destroy not recognising widgets that are created and packed/"gridded" on the same line,
    #I split the grid function to the next line for welcomeMessage and inputField.
    welcomeMessage = Label(root, text = 'Welcome to HANGMAN. Please guess the secret word.')
    welcomeMessage.grid(row = 1, columnspan = 5)
    Label(root, text = images[position]).grid(row = 3, columnspan = 5)
    Label(root, text = secretWord).grid(row = 5, columnspan = 5)
    Label(root, text = guessedLetters).grid(row = 7, columnspan = 5)
    submitButton = Button(root, text = 'Submit', command = onSubmitCheckGuess).grid(row = 9, column = 1)
    inputField = Entry(root, textvariable = variableString)
    inputField.grid(row = 9, column = 2)
    print(guessed)

def listToString():
    for dash in dashes:
        secretWord = secretWord + dash
    for letter in guessed:
        guessedLetters = guessedLetters + letter + ' '

def getGuess():
    guess = variableString.get()
    return(guess)       

def onSubmitCheckGuess():
    global welcomeMessage, inputField, errors, correct
    firstGuess = True
    guess = getGuess()
    i = 0
    result = []
    print(guessed)
    print('.')
    if guess in guessed:
        firstGuess = False
        welcomeMessage.destroy()
        welcomeMessage = Label(root, text = 'You have already guessed that letter.')
        welcomeMessage.grid(row = 1, columnspan = 5)
        inputField.destroy()
        inputField = Entry(root, textvariable = variableString)
        inputField.grid(row = 9, column = 2)
        return(True)
    else:
        welcomeMessage.destroy()
    if errors < 6:
        for letter in goal:
            if guess == letter:
                if guess not in guessed:
                    dashes[i] = guess + ' '                    
                    welcomeMessage = Label(root, text = 'Correct!')
                    welcomeMessage.grid(row = 1, columnspan = 5)
                    correct = correct - 1
            i = i + 1
        if guess not in goal:
            welcomeMessage = Label(root, text = 'Incorrect!')
            welcomeMessage.grid(row = 1, columnspan = 5)
            errors = errors + 1
        guessed.append(guess)
        print(dashes)
    result.append(correct)
    result.append(errors)
    return(result)

if __name__ == '__main__':
    startGame()
    TkGUI(0)
    root.mainloop()
