# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

words=["car", "roadrunner", "dinosaur"]
guess_words = random.choice(words)

c=guess_word[:] # will make a copy of the selected guessword
indexes=[] # for use in detector function
correct_ans=list(guess_word)

def hint_gen():
    a= "roadrunner"
    for i in range(0,len(a),3): #range from 0 to length with increments of 3 to get every third letter
        b = random.choice(a) #replacing underscore with hint letter

name=input("Enter your name: ")#name input functionality
print(f"Hello {name}, Welcome to Hangman!") # formatted strings
print(list(guess_word))

guess=input("Guess a letter: ")
for i in list(guess_word):
     if guess==i:
         print(guess)

pics= ['''
     +---+
         |
         |
         |
        ===''', '''
    +---+
    O    |
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

print(pics[6])