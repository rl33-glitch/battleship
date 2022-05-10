# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import random

words = ["cat", "four", "spots"]
secret_word = random.choice(words)

guessed_so_far = len(secret_word) * "_ "


while True:
    print(guessed_so_far)

    guess = input("I'm thinking of a word, can you guess a letter?: ")

    if guess in secret_word:
        print("You guessed correctly")
