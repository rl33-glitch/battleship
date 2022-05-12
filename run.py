# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import random

def animation(incorrect,board):
    if incorrect == 0:
        print(board)
    
    elif incorrect == 1:
        print ("      _________")
        print ("     |/")
        print ("     |")
        print ("     |")
        print ("     |")
        print ("    _|_")

words = ["cat", "four", "spots"]
secret_word = random.choice(words)

guessed_so_far = len(secret_word) * "_ "


while True:
    print(guessed_so_far)

    guess = input("I'm thinking of a word, can you guess a letter?: ")

    if guess in secret_word:
        print("You guessed correctly")
