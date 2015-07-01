# Hangman game
#

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if getGuessedWord(secretWord, lettersGuessed) == secretWord:
        return True
    return False
        

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    goodLetters = []
    for letters in secretWord:
        if letters in lettersGuessed:
            goodLetters.append(letters)
        else:
            goodLetters.append('_ ')
    return ''.join(goodLetters)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = list(string.ascii_lowercase)
    for lettersA in lettersGuessed:
        if lettersA in allLetters: 
            allLetters.remove(lettersA)
    return ''.join(allLetters)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'    
    guesses = 8
    lettersGuessed = []
    while guesses > 0:
        print  '-----------' 
        print 'You have ' + str(guesses) + ' guesses left'
        print 'Available Letters: ' + getAvailableLetters(str(lettersGuessed))
        letterGuess = raw_input('Please guess a letter: ').lower() 
        if letterGuess not in lettersGuessed:
            lettersGuessed.append(letterGuess)        
            if letterGuess not in secretWord:
                print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
                guesses -= 1                               
            else:                   
                print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
                if isWordGuessed(secretWord, lettersGuessed):
                    print '-------------'
                    print 'Congratulations, you won!'
                    break
                
        else:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed) 
        if guesses <= 0:
            print  '-----------'
            print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
            break
        
           
        
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! 

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)
