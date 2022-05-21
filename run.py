# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random


words=["car","roadrunner","dinosaur"]
guess_word=random.choice(words)




c=guess_word[:] # will make a copy of the selected guessword
correct_ans=guess_word

indexes=[] # for use in detector function
guess_word=list(guess_word)

def hard(guess_word):
    d=""
    for i in range(len(guess_word)):
        d+="_"
    return d

pics= ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
    |   |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
      ===''']

