

## Hangman

I created a simple well known word guessing game called hangman. It was designed to show some basic python knowledge with the interface being the python terminal. The user will try and guess a randomely selected word by inputting one letter at a time which will either reveal the word or lead to a loss if the word was not guessed. The player will have 6 chances and the game includes 2 game modes which are easy and hardcore. The easy gamemode will display some random letters which in turn will help the player guess the word.

https://hangman-12.herokuapp.com/ - LInk to live site here

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
