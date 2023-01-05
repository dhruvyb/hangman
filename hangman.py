#! python3

import random, re

def hangmanDiagram(step):
    if step == 0:
        print('','\n')
    if step == 1:
        print('''
   
   |     
   |     
   |    
   |    
   |    
   |

''')
    if step == 2:
        print('''
   _______
   |     
   |     
   |    
   |    
   |    
   |

''')
    if step == 3:
        print('''
   _______
   |    
   |    
   |    
   |     
   |    
   |__

''')
    if step == 4:
        print('''
   _______
   | /    
   |/     
   |    
   |    
   |    
   |__

''')
    if step == 5:
        print('''
   _______
   | /   |
   |/    
   |    
   |    
   |    
   |__

''')
    if step == 6:
        print('''
   _______
   | /   |
   |/    O
   |   
   |   
   |   
   |__

''')
    if step == 7:
        print('''
   _______
   | /   |
   |/    O
   |     |
   |     |
   |     
   |__

''')
    if step == 8:
        print('''
   _______
   | /   |
   |/    O
   |    /|
   |     |
   |    
   |__

''')
    if step == 9:
        print('''
   _______
   | /   |
   |/    O
   |    /|\\
   |     |
   |   
   |__

''')
    if step == 10:
        print('''
   _______
   | /   |
   |/    O
   |    /|\\
   |     |
   |    / 
   |__

''')
    if step == 11:
        print('''
   _______
   | /   |
   |/    O
   |    /|\\
   |     |
   |    / \\
   |__

''')

listOfWords = ['hello', 'dhruvesh', 'hangman', 'computer', 'pizza'] #list of words

word = random.choice(listOfWords) #pick random word
wordList = list(word)               #convert to list
guessedLettersWord = []
for i in wordList:
    guessedLettersWord.append('_')      #create list of gaps to display
numberOfGuesses = range(1,12)
guessedLetters = []
incorrectGuess = 0
guessesLeft = 11
correctLetters = 0

guessRegex = re.compile(r'[a-zA-Z]{1}')

print("HANGMAN GAME", end='\n')
print("I'm thinking of a word. You have " + str(guessesLeft) + " guesses.", end='\n')

while incorrectGuess < 11:
    
    if correctLetters == len(word):
        break
        
    for letter in guessedLettersWord:
        print(letter, end=' ')
    print('\n')
    while True:
        guess = input('Make a guess: ')
        if len(guess) != 1:     # single character
            print('Please enter a single letter.','\n')
            continue
        guessMatch = guessRegex.search(guess)       #letter match regex
        if guessMatch == None:
            print('Please enter a letter','\n')
            continue
        if guess in guessedLetters:     # already made a guess
            print('You have guessed that letter already. Please try again.', '\n')
            continue
        break

    guessedLetters.append(guess)
    correctGuess = 0
    wordIndex = 0

    for letter in word:
        wordIndex += 1
        if guess.lower() == letter.lower():
            correctGuess += 1
            correctLetters += 1
            guessedLettersWord[wordIndex - 1] = letter.upper()

    if correctGuess > 0:
        print('Correct!', '\n')
    else:
        incorrectGuess += 1
        guessesLeft -= 1
        print('Sorry. That letter is not correct. You have ' + str(guessesLeft) + ' guesses left.', '\n')
        hangmanDiagram(incorrectGuess)



if incorrectGuess == 11:
    print('Sorry, you lost. The answer was ' + word.upper())
elif incorrectGuess < 11:
    for letter in guessedLettersWord:
        print(letter, end=' ')
    print(''' 
Congratulations! You won!''')
