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

def TkGUI():
    global errors, inputField, variableString, welcomeMessage, inputField, submitButton, secretWord, guessedLetters, secretWordLabel, guessedLettersLabel, gallowsImages
    variableString = StringVar()
    for dash in dashes:
        secretWord = secretWord + dash
    for letter in guessed:
        guessedLetters = guessedLetters + letter + ' '
    #Due to TKinter destroy not recognising widgets that are created and packed/"gridded" on the same line,
    #I split the grid function to the next line for all the modules that I later want to change or destroy.
    welcomeMessage = Label(root, text = 'Welcome to HANGMAN. Please guess the secret word.')
    welcomeMessage.grid(row = 1, columnspan = 5)
    gallowsImages = Label(root, text = images[errors])
    gallowsImages.grid(row = 3, columnspan = 5)
    secretWordLabel = Label(root, text = secretWord)
    secretWordLabel.grid(row = 5, columnspan = 5)
    guessedLettersLabel = Label(root, text = guessedLetters)
    guessedLettersLabel.grid(row = 7, columnspan = 5)
    submitButton = Button(root, text = 'Submit', command = onSubmitCheckGuess).grid(row = 9, column = 1)
    inputField = Entry(root, textvariable = variableString)
    inputField.grid(row = 9, column = 2)

def getGuess():
    guess = variableString.get()
    return(guess)       

def onSubmitCheckGuess():
    global position, welcomeMessage, inputField, errors, correct, secretWord, secretWordLabel, guessedLettersLabel, gallowsImages
    if errors < 6 and correct != 0:
        guessedLetters = 'Guessed Letters: '
        secretWord = 'Secret Word: '
        guess = getGuess()
        i = 0
        result = []
        if guess in guessed:
            welcomeMessage.destroy()
            welcomeMessage = Label(root, text = 'You have already guessed that letter.')
            welcomeMessage.grid(row = 1, columnspan = 5)
            return()
        else:
            welcomeMessage.destroy()
        if errors < 6:
            for letter in goal:
                if guess == letter:
                    if guess not in guessed:
                        dashes[i] = guess + ' '                    
                        welcomeMessage = Label(root, text = 'Correct!')
                        welcomeMessage.grid(row = 1, columnspan = 5)
                        correct -= 1
                i = i + 1
            guessed.append(guess)
        if guess not in goal:
            welcomeMessage = Label(root, text = 'Incorrect!')
            welcomeMessage.grid(row = 1, columnspan = 5)
            errors += 1
        secretWordLabel.destroy()
        guessedLettersLabel.destroy()
        gallowsImages.destroy()
        for dash in dashes:
            secretWord = secretWord + dash
        for letter in guessed:
            guessedLetters = guessedLetters + letter + ' '
        secretWordLabel = Label(root, text = secretWord)
        secretWordLabel.grid(row = 5, columnspan = 5)
        guessedLettersLabel = Label(root, text = guessedLetters)
        guessedLettersLabel.grid(row = 7, columnspan = 5)
        gallowsImages = Label(root, text = images[errors])
        gallowsImages.grid(row = 3, columnspan = 5)
    if errors == 6 or correct == 0:
        welcomeMessage.destroy()
        if correct == 0:
            Label(root, text = 'You Won!').grid(row = 1, columnspan = 5)
        elif errors == 6:
            Label(root, text = 'You Lost!').grid(row = 1, columnspan = 5)

if __name__ == '__main__':
    startGame()
    TkGUI()
    root.mainloop()
