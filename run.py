# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

words=["car", "roadrunner", "dinosaur"]
guess_words = random.choice(words)

def hint_gen():
    a= "roadrunner"
    for i in range(0,len(a),3):#range from 0 to lenght with increments of 3 to get every third letter
        b = random.choice(a)#replacing underscore with hint letter