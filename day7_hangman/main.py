# Freddy B. MIT License
# No liability accepted

# built-in modules
from random import randint
import re

# 3rd-party modules

# my-own modules
from hangman_unicode_art import logo, stages
from words import word_list

# Pick a word
play_word = word_list[randint(0, len(word_list)+1)]
print(play_word)

# Create a new string with underscores per each letter of the play word
EMPTY_CHAR = "_"
empty_word = ""
for letter in range(len(play_word)):
    empty_word += EMPTY_CHAR

# Request user to enter a letter
players_choice = input("Please enter a letter: ").lower()

# is the letter in the word?
if players_choice in play_word:
    # regular expressions module
    letter_positions = [item.start() for item in re.finditer(players_choice, play_word)]
    play_word = list(play_word)
    empty_word = list(empty_word)
    for letter_position in letter_positions:
        empty_word[letter_position] = players_choice

    empty_word = "".join(empty_word)

    # are there letters to guess?
    if EMPTY_CHAR in empty_word:
        print("loop again")
    else:
        print("You win")
        # call if you want to play again


else:
    # call function to add a hangman part, remove one guess attempt
    print("crazy")

# print(letter_positions)
# print(empty_word)



