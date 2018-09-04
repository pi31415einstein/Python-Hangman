from random import randrange                                #
words = []                                                  #Words is a list of the words that the user could be guessing.
dashes = []                                                 #Dashes is a list of how many dashes to display and where the correct letters go.
images = []                                                 #Images is the list of images which are read from an external file.
guessed = []                                                #Guessed is a list of which letters the user has guessed.
position = 0                                                #Position is how many errors the user has made, used to determine which image to display.

for word in open('words.txt'):                              #Opens file with list of words
    words.append(word.rstrip())

images = open('images.txt').read()                          #Opens file with hangman images and creates list with each image
images = images.split(',')

def printStage(position):                                   #Prints the images of the noose and the dashes.
    print(images[position])
    for dash in dashes:
        print(dash, end='')
    print()
    print('Guessed Letters: ', end='')
    for letter in guessed:
        print(letter, end=', ')
    print()
def start_game():                                           #Starts the game: selects a word, returns it and prints the dashes.
    i = 0
    goal = words[randrange(len(words))]                     #Selects a random word from the word bank.
    numberOfLetters = correct = len(goal)
    printStage(0)
    while i != numberOfLetters:
        print('_ ', end='')
        dashes.append('_ ')
        i = i + 1
    print()
    return(goal)

def guess(position, correct):                               #Decides if the user should guess a letter and if the letter is in the goal. If the letter is in the goal, removes the corresponding dash and replaces it with the letter.
    i = 0
    result = []
    if position < 6:                                        #Checks if the user has exceeded the number of errors
        guess = input('Please guess a letter: ')
        for letter in goal:
            if guess == letter:
                dashes[i] = guess + ' '
                correct = correct - 1
            i = i + 1
        for dash in dashes:
            print(dash, end='')
        print()
        if guess not in goal:                               #Checks if the selected letter is not in the goal.
            position = position + 1                         #Increases the number of errrors by 1.
        guessed.append(guess)                               #Adds the guessed letter to the list of guesses.
    print()
    result.append(correct)
    result.append(position)
    return(result)

goal = start_game()
correct = len(goal)

while position < 6 and correct > 0:
    output = guess(position, correct)
    print()
    print('---------------------------------------------')
    print()
    print()
    correct = output[0]
    position = output[1]
    printStage(position)
print()
print('---------------------------------------------')
print()
if position == 6:
    print('You lost')
else:
    print('You won')
input()
