from tkinter import *
from os import system
from random import randrange

root = Tk()
words = []
images = []
dashes = []
secretWord = 'Secret Word: '
guessedLetters = 'Guessed Letters: '
errors = 0

for word in open('words.txt'):
    words.append(word.rstrip())

images = open('images.txt').read()
images = images.split(',')

def startGame():
    i = 0
    goal = words[randrange(len(words))]
    numberOfLetters = correct = len(goal)
    while i != numberOfLetters:
        dashes.append('_ ')
        i = i + 1
    return(goal)

def TkGUI(position):
    Label(root, text = 'Welcome to HANGMAN. Please guess the secret word.').grid(row = 1, columnspan = 5)
    Label(root, text = images[position]).grid(row = 3, columnspan = 5)
    Label(root, text = secretWord).grid(row = 5, columnspan = 5)
    Label(root, text = guessedLetters).grid(row = 7, columnspan = 5)
    Button(root, text = 'Submit', command = checkGuess).grid(row = 9, column = 1)
    inputField = Entry(root, text = 'Guessed Letter').grid(row = 9, column = 2)

def listToString():
    for dash in dashes:
        secretWord = secretWord + dash
    for letter in guessed:
        guessedLetters = guessedLetters + letter + ' '

def getGuess():
    guess = guessEntry.get()
    return(guess)

def reGuess():
    root.destroy()
    Label(root, text = 'Yoy have already guessed that letter.').grid(row = 1, columnspan = 5)
    Button(root, text = 'Submit', command = getGuess).grid(row = 3, column = 1)
    inputField = Entry(root, text = 'Guessed Letter').grid(row = 3, column = 2)

def checkGuess():
    i = 0
    result = []
    guess = inputField.get()
    if errors < 6:
        while guess in guessed:
            guess = reGuess()
        for letter in goal:
            if guess == letter:
                if guess not in guessed:
                    dashes[i] = guess + ' '
                    correct = correct - 1
            i = i + 1
        if guess not in goal:
            errors = errors + 1
        guessed.append(guess)
    result.append(correct)
    result.append(errors)
    return(result)

startGame()
TkGUI(0)
checkGuess()
root.mainloop()

