
from random import choice
from turtle import Turtle, Screen

from numpy import tile
from back import drawing_the_hangman, prompt, get_word
import easygui

# getting the word using api


# game code
def word_to_guess(word):
    # making the word into a list of its letter
    word_list = list(word)
    
    
    # creating a hash map in which each letter has in the word is matched with their index in a list like "a : [1,3]"
    word_hash = {}
    for index in range(len(word_list)):
        if word_list[index] in word_hash.keys():
            word_hash[word_list[index]].append(index)
        else:
            word_hash[word_list[index]] = [index]
            
    #transforming the word into dashed word to hide the letter from the player, it will display as "_____"
    word_to_guess_dashed = ["_" for _ in range(len(word_list))]
    word_to_guess_str = "".join(word_to_guess_dashed)
    
    #a counter to keep in track the number of letter found (score) by the player and the attempt they have left
    letter_found_counter = 0
    attempt = 5
    while attempt:
        # criteria to win the game, if the # of letter found match the lenght of the letter we win and a msg box pops u[]
        if letter_found_counter == len(word_to_guess_str):
            return easygui.msgbox(title= "Mystery solved!", msg= f"You found the word, it was {word}", ok_button="OK")
        #user input   
        user_input = prompt(prompt= f"Guess the word: {word_to_guess_str} ---- you have {attempt} left")
        
        # check if the letter guessed is our keys, 
        #if so the key is holding the index where we going to put the words on our dashed word
        # indexes are stored in a list so we take each of them go to the position and put the letter there and increment the counting
        # join the list and return it to the user as a feedback that they found a letter
        
        if user_input in word_hash.keys():
            for index in word_hash[user_input]:        
                word_to_guess_dashed[index] = user_input
                letter_found_counter+=1
            word_to_guess_str = "".join(word_to_guess_dashed) 
            
            
        # if the letter isn't in the key, the letter is wrong
        # then we have our drawer, that follow steps, drawthe the hangman
        else:
            drawing_the_hangman(attempt)
            attempt-=1
    return easygui.msgbox(title = "You have been hanged! ",msg=f"You failed, the word to guess was {word}")
    
screen = Screen()
screen.setup()
word = choice(get_word())
word_to_guess(word)
screen.exitonclick()

