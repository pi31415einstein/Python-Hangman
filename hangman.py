from random import randrange                                #Randrange is used to select a word.
from os import system                                       #System is used to clear the screen.
words = []                                                  #Words is a list of the words that the user could be guessing.
dashes = []                                                 #Dashes is a list of how many dashes to display and where the correct letters go.
images = []                                                 #Images is the list of images which are read from an external file.
guessed = []                                                #Guessed is a list of which letters the user has guessed.
position = 0                                                #Position is how many errors the user has made, used to determine which image to display.
                                                            #This line is meant to be empty (makes the code look good).
for '''every''' word in open('words.txt'):                  #Opens file with list of words
    words.append(word.rstrip())                             #Adds the word from the file to the list and removes any spaces.
                                                            #This line is meant to be empty (makes the code look good).
images = open('images.txt').read()                          #Opens file with hangman images and creates list with each image
images = images.split(',')                                  #creates a list for the images from the file that contains the images
def start_game():                                           #Starts the game: selects a word, returns it and prints the dashes.                                                   #
    i = 0                                                   #Sets i to 0.
    goal = words[randrange(len(words))]                     #Selects a random word from the word bank.
    numberOfLetters = correct = len(goal)                   #Sets variables numberOfLetters and correct to the number of letters in the secret word/goal
    while i != numberOfLetters:                             #Populates the list dashes with dashes and prints them out 
        dashes.append('_ ')                                 #Appends the dashes to the list
        i = i + 1                                           #Increments the counter.
    print()                                                 #Prints a newline
    printStage(0, goal)                                     #Prints the images, dashes and the guessed letters.
    return(goal)                                            #returns the chosen goal.
                                                            #This line is meant to be empty (makes the code look good).
def printStage(position, goal):                             #Prints the images of the noose and the dashes.
    i = 0                                                   #Resets i to zero.
    numberOfLetters = len(goal)                             #Sets the variable numberOfLetters to the number of letters in the goal.
    print(images[position])                                 #Prints the first image of the gallows
    print('\nSecret Word: ', end='')                        #Prints the words 'Secret Word:'
    for '''each''' dash in dashes:                          #Loops around the print statement for every item in the dashes list.
        print(dash, end='')                                 #Prints the contents of the list dashes.
    print('\n')                                             #prints two newlines.
    print('Guessed Letters: ', end='')                      #Prints the guessed letters list
    if len(guessed) == 0:                                   #Checks if the user has or hasn't 
        print('None')                                       #Prints 'None' if the user hasn't guessed any letters.
    for '''each''' letter in guessed:                       #Loops around the contents of the list of letters that the user has guessed.
        print(letter, end=' ')                              #Prints the letters that the user guesses.
    print()                                                 #Prints out another newline to make the output look good.
                                                            #This line is meant to be empty (makes the code look good).
def guess(position, correct):                               #Decides if the user should guess a letter and if the leter is in the goal. If the letter is in the goal, removes the corresponding dash and replaces it with the letter.
    i = 0                                                   #Resets the counter i to zero.
    result = []                                             #Creates an empty list for the output.
    if position < 6:                                        #Checks if the user has exceeded the number of errors
        guess = input('Please guess a letter: ')            #Asks the user for their guess.
        while guess in guessed:                             #Checks if the guess has been guessed previously.
            print('You have already guessed the letter.')   #Notifies the user that they have already guessed the said letter.
            guess = input('Please guess another letter: ')  #Asks the user for another letter.
        for '''each''' letter in goal:                      #Checks if the guessed letter matches the letters in the goal
            if guess == letter:                             #Checks if the guess matches the individual letters in the goal.
                if guess not in guessed:                    #Checks if the guessed letters have not already been guessed
                    dashes[i] = guess + ' '                 #Replaces a dash in the appropriate location with the correct letter.
                    correct = correct - 1                   #Lowers the count of how many letters remain.
            i = i + 1                                       #Increases the counter regardless of being correct or not.
        for '''each''' dash in dashes:                      #Loops around the print statement for every item in the dashes list.
            print(dash, end='')                             #Prints the contents of the list dashes.
        print()                                             #Prints a newline to make the output look good.
        if guess not in goal:                               #Checks if the selected letter is not in the goal.
            position = position + 1                         #Increases the number of errrors by 1.
        guessed.append(guess)                               #Adds the guessed letter to the list of guesses.
    print()                                                 #Also prints a newline to make the output look good.
    result.append(correct)                                  #Compresses the output into a list, value zero is how many correct letters.
    result.append(position)                                 #Second value in the list is how many errors the user has made.
    return(result)                                          #Returns the list
                                                            #This line is meant to be empty (makes the code look good).
print('Welcome to HANGMAN. Please try to guess the secret word.', end='\n\n')   #Prints the welcome message.
goal = start_game()                                         #Starts the game and selects a word.
correct = len(goal)                                         #Defines the length of the goal
                                                            #This line is meant to be empty (makes the code look good).
while position < 6 and correct > 0:                         #Checks if the user has already finished the game by winning or losing.
    output = guess(position, correct)                       #Output is a list that contains the counter of how many correct letters the user has correctly guessed and how many 
    print()                                                 #Prints a newline before the dividing line.
    print('---------------------------------------------')  #This is a line that divides the hangman output and the you win or lose message.
    print()                                                 #Prints a newline after the dividing line.
    system('cls')                                           #Clears the screen if the program is run as a standalone but if it ran via IDLE it wont clear the screen.
    correct = output[0]                                     #Splits the output list into two variables.
    position = output[1]                                    #Splits the output list into two variables.
    printStage(position, goal)                              #Prints the gallows, dashes and guessed letters.
    print()                                                 #Prints a newline to mmake the output look good.
print('---------------------------------------------')      #Prints dashes to make the output look good.
print()                                                     #Prints a newline to make the moutput look good.
if position == 6:                                           #Checks if the user has made enough errors to lose.
    print('You lost')                                       #Prints the 'You lost' message.
else:                                                       #Else, print the you won message.
    print('You won')                                        #Prints the 'You won' message.
input()                                                     #Final input command to prevent the window from closing.
