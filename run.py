# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

words=["car", "roadrunner", "dinosaur"]
guess_words = random.choice(words)

c=guess_word[:] 
indexes=[] 
guess_word=list(guess_word)
correct_ans=guess_word

def hint_gen(guess_word,c):
    for i in range(0,len(guess_word),3): 

        c=c.replace(c[i],"_")
    return c
    
c=hint_gen(guess_word,c) 

name=input("Enter your name: ")
print(f"Hello {name}, Welcome to Hangman!") 
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