#Name: Addie Murphy
#Class: CSC 110

#Program Title: Wordle

#General Solution:
"""
The computer will import a list of five letter words from a dictionary. It will choose
a random word to use for the game. The player will input a word guess and the computer
will compare the letters of the two words to see if each letter is correct, incorrect,
or in the wrong spot. The player will have six guesses and their score is computed based
on how many guesses it took to guess the correct word. It will ask if they want to play
again. If so, the program starts over again with a different word

"""

#Pseudocode:
"""
Computer chooses a random word
while the word has not been guessed and player has not used all 6 guesses
    Player guesses a word
    For the length of the word
        Computer checks each letter to see if it is correct
        If letter is not in word
            Print X
        Elif letter is in word but not right space
            Print Y
        Else letter is in right place
            Print G
    Add a guess to counter
Compute overall score
Print score
Ask if player would like to play again
    If yes
        Run program again
    Else
        Print goodbye and end program
    
"""

#Functions:
import random

def getData():
    
    #This function reads in the list of five letter words and returns a list of all the words

    wordList = []
    goodFile = False

    while goodFile == False:
        fname = input("Please enter a file name: ")
        try:
            wordFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name try again...")

    for line in wordFile:
        line = line.strip()
        wordList.append(line)

    wordFile.close()
    
    return wordList

def getWord(wordList):

    #This function chooses a random word from the wordList to use in the game by using the randint function.
    
    wordIndex = random.randint(0, len(wordList)-1)
    worldWord = wordList[wordIndex]
    
    return worldWord

def computeClue(guessWord, worldWord):

    #This function takes the word returned from the getWord function and compares
    #it to the word that is input from the player. It has a for loop that runs through the length
    #of the word and checks each letter to replace an X with a G if it is correct. It has another
    #for loop that checks to see if the letter is in the worldWord and is not already correct, and
    #then replaces an X with a Y. Otherwise the letter is wrong and stays as an X

    clue = "XXXXX"
    
    for i in range(len(guessWord)):
        if guessWord[i] == worldWord[i]:
            clue = clue[:i] + 'G' + clue[i+1:]
            worldWord = worldWord[:i] + '$' + worldWord[i+1:]
    
    for j in range(len(guessWord)):
        if guessWord[j] in worldWord and clue[j] != 'G':
            clue = clue[:j] + 'Y' + clue[j+1:]

    return clue

def isGuessInDictionary(worldWord, wordList):

    #This function takes in an input guess from the player and makes it uppercase. If the word is not
    #in the wordList, it will print an error and re-ask the player for an input. Otherwise, it breaks out
    #of the function and returns the player's guess
    
    goodWord = False
    
    while goodWord == False:
        guessWord = input("Make a guess: ")
        guessWord = guessWord.upper()
        if guessWord not in wordList:
            print("Word not in dictionary - try again...")
        else:
            goodWord = True
 
        
    return guessWord

def computeGuess(worldWord, wordList):
    
    #This function computes the guessWord from the guessInDictionary function, and computes the clue
    #from the computeClue function. It then prints the guess and the clue. If the word is correct, it will
    #break out of the loop. Otherwise i is incremented and another guess is added. The number of guesses is
    #returned to then compute the score in the getScore function
    
    i = 0
    goodWord = False

    while i < 6 and goodWord == False:
        guessWord = isGuessInDictionary(worldWord, wordList)
        clue = computeClue(guessWord, worldWord)
        print(guessWord)
        print(clue)
        if guessWord == worldWord:
            goodWord = True
        else:
            i+= 1
            
    guesses = i+1
        
    return guesses

def getScore(guesses, worldWord):

    #This function computes the score. The score is set equal to the number of guesses first. If the word
    #is guessed then the score is returned as the number of guesses. If the word is not guessed in the 6
    #guesses allowed, the score is 10 and the word is given to the player.
    
    score = guesses
    if score >= 6:
        print("Sorry, you did not guess the word: ", worldWord)
        score = 10
    else:
        print('\nCongratulations, your wordle score for this game is ', score)
            
    return score

def playAgain():

    #This function ask sif the player wants to play again. If yes, then the loop in the main function will
    #run the game again. Otherwise, it will print Thanks for playing! and end the game. 
    
    YorN = input("\nWould you like to play again (Y or N)?")

    if YorN == 'n' or YorN == 'N':
        print("\nThanks for playing!")
    
    return YorN

def main(seedValue):
    random.seed(seedValue)
    wordList = getData()
    worldWord = getWord(wordList)
    guesses = computeGuess(worldWord, wordList)
    score = getScore(guesses, worldWord)
    print('Your overall score is ', score)
    overallScore = score
    YorN = playAgain()
    
    while YorN == 'y' or YorN == 'Y':
        worldWord = getWord(wordList)
        guesses = computeGuess(worldWord, wordList)
        score = getScore(guesses, worldWord)
        overallScore = overallScore + score
        print('Your overall score is ', overallScore)
        YorN = playAgain()
    
    return
