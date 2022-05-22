

## Hangman

I created a simple well known word guessing game called hangman. It was designed to show some basic python knowledge with the interface being the python terminal. The user will try and guess a randomely selected word by inputting one letter at a time which will either reveal the word or lead to a loss if the word was not guessed. The player will have 6 chances and the game includes 2 game modes which are easy and hardcore. The easy gamemode will display some random letters which in turn will help the player guess the word.

https://hangman-12.herokuapp.com/ - LInk to live site here

# Content
- [How to Play]()
- [Features]()
- [Lucid Chart]()
- [Technologies used]()
- [Validator]()
- [Deployment]()
- [Credits]()


# How to play

- The User will enter there name which will then take them to a options menu with the options being Easy mode, Hardcore mode, and How to play.
- The User will then choose a letter if the letter is part of the word then it will fill in the space where it belongs in the word.
- If the letter that is chosen is not part of the word then one of the 6 moves the player has is lost and the hangman animation will progress
- If the user selects 6 wrong letters then its game over 
- If the user selects the easy game mode then some of the letters in the word will already be visible.
- If hardcore mode is selected then no hints will be given.

 

# Features

- The User will be presented with a enter name input under a hangman display 

![image](https://user-images.githubusercontent.com/67274642/169688458-3efb485f-004b-4d9c-8754-39c9559c85e9.png)

- The User will then be greeted with there name and presented with the 3 options 1 will take them to the easy mode which includes hints
2 will take them to the hardcore gamemode which does not include hints and 3 will present simple instructions. 

![image](https://user-images.githubusercontent.com/67274642/169689058-cd62d61b-4089-42a0-8876-18759da926a9.png)

- The how to play option consists of 3 lines giving a simple outline of how the game works.

![image](https://user-images.githubusercontent.com/67274642/169689243-2b15d0a2-180d-40a5-8e14-f86a0c1737cf.png)

- The easy game mode will have some of the letters already filled in giving the user a big clue and making it a easy experience

![image](https://user-images.githubusercontent.com/67274642/169689341-22b6d4d9-593d-4d4e-891d-ae36a855365f.png)

- The hardcore game mode does not give the user any hints which means the user will be starting from scratch.

![image](https://user-images.githubusercontent.com/67274642/169689411-48be2c42-7697-4d09-9a30-9a07eea8fd81.png)

- If the user guesses a letter which is correct it will display in the word the user is trying to guess.

![image](https://user-images.githubusercontent.com/67274642/169689500-8585ab21-2068-4f74-bb9b-8c2e84545cd7.png)

- If the user guesses a letter which is not part of the word then that letter will be displayed in a Letters Used area and the first animation of the hangman board will be displayed.

![image](https://user-images.githubusercontent.com/67274642/169689566-200bbec3-91b1-486c-a93d-7b2a7b9fe98e.png)

- If the user guesses incorrectly and uses up there lives then the caption you loose will appear and the word will be revealed without the 
correctly guessed letters.

![image](https://user-images.githubusercontent.com/67274642/169689723-0603c1c9-ccf1-4d8e-bcce-78e9c47a656a.png)

- If the user inputs a wrong datatype like a number or two letters together then the caption please enter a letter will appear and prompt the user to retry.

![image](https://user-images.githubusercontent.com/67274642/169689778-5a7de351-c338-4300-bbcf-61d212ac213d.png)

- If the user guesses the word correctly a you win display will appear and the 3 options menu will appear again.

![image](https://user-images.githubusercontent.com/67274642/169689938-49bf936c-1e41-4b03-a225-6377ac7d2cda.png)

- If the user inputs the incorrect data type for the menu such as a letter then the user will be prompted to reenter a number from 1-3.

![image](https://user-images.githubusercontent.com/67274642/169689984-31478b9e-eb73-481e-91b6-fc303b66d604.png)








# Lucid Chart

![image](https://user-images.githubusercontent.com/67274642/169691273-3fdab53b-7616-4567-9686-409e45296234.png)


# Technologies used

- Python(including random word libary)
- Gitpod
- Heroku 
- Lucid flowchart generator 

# Validator
- Pep8 http://pep8online.com/checkresult

![image](https://user-images.githubusercontent.com/67274642/169691392-e2651932-4244-4527-b10e-dcd9832b8630.png)


# Deployment

- Created a new account on heroku

# Credits






