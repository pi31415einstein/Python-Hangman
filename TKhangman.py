from tkinter import *
from os import system
from random import randrange

root = Tk()
words = []
images = []
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

def listToString():
    for dash in dashes:
        secretWord = secretWord + dash
    for letter in guessed:
        guessedLetters = guessedLetters + letter + ' '

def getGuess():
    guess = guessEntry.get()
    return(guess)

def ReGuess():
    root.destroy()
    Label(root, text = 'Yoy have already guessed that letter.').grid(row = 1, columnspan = 5)
    Button(root, text = 'Submit', command = getGuess).grid(row = 3, column = 1)
    guessEntry = Entry(root, text = 'Guessed Letter').grid(row = 3, column = 2)

def checkGuess(guess, errors):
    i = 0
    result = []
    if errors < 6:
        guess = getGuess()
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

def TkGUI(position):
    Label(root, text = 'Welcome to HANGMAN. Please guess the secret word.').grid(row = 1, columnspan = 5)
    Label(root, text = images[position]).grid(row = 3, columnspan = 5)
    Label(root, text = secretWord).grid(row = 5, columnspan = 5)
    Label(root, text = guessedLetters).grid(row = 7, columnspan = 5)
    

TkGUI(0)

root.mainloop()
