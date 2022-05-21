# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random


words = ["car","roadrunner","dinosaur"]
guess_word = random.choice(words)




c=guess_word[:] # will make a copy of the selected guessword
correct_ans = guess_word

indexes = [] # for use in detector function
guess_word = list(guess_word)

def hard(guess_word):
    d = ""
    for i in range(len(guess_word)):
        d += "_"
    return d

def hint_gen(guess_word,c): # creating the word with hints
    for i in range(0,len(guess_word),3): # i will be used as index numbers
                                         # range from 0 to lenght 0-9 with step size of three to get every third letter    
        c = c.replace(c[i],"_") # selection for replacing with a dash
    return c

def detector(guess_word,guess): # gives the index positions where guessword is present 
    a = []
    guess_word = list(guess_word)
  
    count = 0
    for i in guess_word:
        if i == guess:
            a.append(count) # adding the count which is representing the index to the end of list a
        count += 1
    return a # indexes where the guess word is present

def modifier(c,guess_word = "roadrunner",guess = "r"): # it will replace the dashes with the correctly guessed letter
    a = detector(guess_word,guess) # positions of the guessed letter
    c = list(c) # c is the word with the dashes which is converted into a list here for easy manipulation
    r = "" # will be modified c where the dashes are replaced back with the correctly guessed letter
   
    for i in a:
        c[i] = guess
        guess_word[i] = "_" # guess word will now have dashes to avoid repetition later on
    for j in c: # converting the list c into a string r
        r = r + j
    return r #  creating modified c


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



tries = 7 # number of goes player has
animation = 0
letters_used = ""
name = False

while True:
    if name == False:
        name = input("Enter your name: ")
        print(f"Hello {name}, Welcome to Hangman!") # formatted strings
    mode = input("Choose your mode, press (1) for Easy mode, press (2) for Hardcore press (3) for How to play:  ")
    if mode == "1":# if 1 is selected hint gen will be called and a word with hints will be generated
        c = hint_gen(guess_word,c)
    elif mode == "2":#for hardcore mode if 2 is selected 
        c = hard(guess_word)
    elif mode == "3":
        print("How to play instructions blablabla")
        continue
        
    else:
        print("Please enter {1,2,3} to select a mode ")
        continue

    while tries>0 and c!=correct_ans:# if tries are greated than 0 and c is not equal to correct ans
        flag = False # indication of whether the user correctly guessed a letter
       
        if c != correct_ans:#if c is not the correct answer print try guess this..
            print("\nTry to guess this word", c,"")
            try:
                guess=input("\nGuess a letter: ")
                tries -= 1 
                # range for letter is 65-90 for uppercase alphabets and 97-122 for lowercase letters
                if ord(guess)<65 or ord(guess)>90 and ord(guess)<97 or ord(guess)>122:
                    print("\nplease enter a letter") 
                    continue
            except TypeError:
                print("\nYou entered too many characters at once , please enter only one character")
                continue

            for i in guess_word:
                if guess == i:
                    print("\nYou guessed ",guess,"correctly")
                    c = modifier(c,guess_word,guess)#replaces _ with correctly guessed letter
                    flag = True
                    
            if flag == False:# if guess if false 
                letters_used = letters_used + " " + guess#if guess is false it will add letter to already used letters on screen 
                print(f"\nLetters Used: {letters_used}")
                print(pics[animation])
                animation += 1

    if c == correct_ans:
        print("\nYou Win!")
    else:
        print("\nYou Lose!, the correct word was ",guess_word)