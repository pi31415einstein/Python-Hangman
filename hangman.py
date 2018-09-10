from random import randrange                                #Randrange is used to select a word.
from os import system                                       #System is used to clear the screen.
words = []                                                  #Words is a list of the words that the user could be guessing.
dashes = []                                                 #Dashes is a list of how many dashes to display and where the correct letters go.
images = []                                                 #Images is the list of images which are read from an external file.
guessed = []                                                #Guessed is a list of which letters the user has guessed.
position = 0                                                #Position is how many errors the user has made, used to determine which image to display.

for word in open('words.txt'):                              #Opens file with list of words
    words.append(word.rstrip())                             #
                                                            #
images = open('images.txt').read()                          #Opens file with hangman images and creates list with each image
images = images.split(',')                                  #
                                                            #
def printStage(position):                                   #Prints the images of the noose and the dashes.
    print(images[position])                                 #
    for dash in dashes:                                     #Print the values in the list of dashes and correct letters.
        print(dash, end='')                                 #
    print()                                                 #
    print('Guessed Letters: ', end='')                      #
    for letter in guessed:                                  #Prints the letters that the user guesses.
        print(letter, end=' ')                              #
    print()                                                 #
def start_game():                                           #Starts the game: selects a word, returns it and prints the dashes.
    i = 0                                                   #
    goal = words[randrange(len(words))]                     #Selects a random word from the word bank.
    numberOfLetters = correct = len(goal)                   #
    printStage(0)                                           #Prints the 0th image of the gallows.
    while i != numberOfLetters:                             #Populates the list dashes with dashes and prints them out
        print('_ ', end='')                                 #
        dashes.append('_ ')                                 #
        i = i + 1                                           #
    print()                                                 #
    return(goal)                                            #
                                                            #
def guess(position, correct):                               #Decides if the user should guess a letter and if the leter is in the goal. If the letter is in the goal, removes the corresponding dash and replaces it with the letter.
    i = 0                                                   #
    result = []                                             #Creates an empty list for the output.
    if position < 6:                                        #Checks if the user has exceeded the number of errors
        guess = input('Please guess a letter: ')            #
        while guess in guessed:                             #Checks if the guess has been guessed previously.
            print('You have already guessed the letter.')
            guess = input('Please guess another letter: ')
        for letter in goal:                                 #Checks if the guessed letter matches the letters in the goal
            if guess == letter:                             #
                if guess not in guessed:                    #Checks if the guessed letters have not already been guessed
                    dashes[i] = guess + ' '                 #
                    correct = correct - 1                   #
            i = i + 1                                       #
        for dash in dashes:                                 #
            print(dash, end='')                             #
        print()                                             #
        if guess not in goal:                               #Checks if the selected letter is not in the goal.
            position = position + 1                         #Increases the number of errrors by 1.
        guessed.append(guess)                               #Adds the guessed letter to the list of guesses.
    print()                                                 #
    result.append(correct)                                  #
    result.append(position)                                 #
    return(result)                                          #
                                                            #
goal = start_game()                                         #Starts the game and selects a word.
correct = len(goal)                                         #Defines the length of the goal

while position < 6 and correct > 0:                         #Checks if the user has already finished the game by winning or losing.
    output = guess(position, correct)                       #Output is a list that contains the counter of how many empty 
    print()                                                 #
    print('---------------------------------------------')  #
    print()                                                 #
    system('cls')                                           #
    correct = output[0]                                     #
    position = output[1]                                    #
    printStage(position)                                    #
print()                                                     #
print('---------------------------------------------')      #
print()                                                     #
if position == 6:                                           #
    print('You lost')                                       #
else:                                                       #
    print('You won')                                        #
input()                                                     #
