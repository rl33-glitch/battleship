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

def detector(guess_word,guess):
    a=[]
    guess_word=list(guess_word)
    #print(r)
    count=0
    for i in guess_word:
        if i==guess:
            a.append(count)
        count+=1
    return a 

def modifier(c,guess_word="roadrunner",guess="r"): 
    a=detector(guess_word,guess) 
    c=list(c) 
    r="" 
    print(c,a) 
    for i in a:
        c[i]=guess
        guess_word[i]="_" 
    for j in c: 
        r=r+j
    return r 

#name=input("Enter your name: ")
#print(f"Hello {name}, Welcome to Hangman!") 
#print(list(guess_word))

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