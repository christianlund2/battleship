# Battleship!

Ahoy! Battleship is a classic game of luck and skill! Fire your cannons at the enemy grid, locate and sink their fleet and rule the high seas! You get 8 shots to sink 5 ships. Will you be victorious or be doomed to the depths of Davy Jones Locker?

A link to the deployed site can be found [here](github link goes here).

![Responsive Preview](./assets/images/responsive-preview.png)

## User Experience

### First Time Users
* As a first time user, I want the intention of the game to be immediately clear and the structure and navigation to be intuitive. 
* As a first time user, I want to know know if I selected the correct grid position after making my choice.
* As a first time user, I want my final score to be displayed and have the option to play again.

### Returning Users
* As a returning user, I want to improve my previous high score and see what new features have been added to the game.

## Design

#### Grid and Ship Size
* I chose to implement a 7x7 grid size for this game because I feel it is a large enough map to make the game difficult without being impossible to find opponent ships. 
* I chose to have ships as a 1x1 square size and positioned randomly on the board to have a true random game setup.
* If the user chooses a shot location not on the grid, the game informs them the coordinates are not valid and to try again.


## Features

* In 'Easy Mode', the user gets 8 shots to fire, in 'Difficult Mode', the user only gets 5 shots.
* Randomized ship locations on playing board.
* Validated user input for shot coordinates - checks initial shots and also for duplicate shot locations.
* If the chosen point is not on the grid, the game tells the user to input a valid position. 
* If the user fires at a position that has already been used, the game informs them the coordinates have been used and to choose again. 
* Informs the user if the selected coordinates are a hit or miss. 
* Informs user the number of shots remaining.
* Informs the user the game is over, either with no remaining shots or that all ships have been destroyed.

* Starting Screen - The game initializes, welcomes the user and asks for the desired difficulty setting.

![Starting image](./assets/images/starting-image.png)

* Game Page - Asks the user to input a set of coordinates to fire on the game board.

![Game Image](./assets/images/game-image.png)

* Results - After selecting a row and column to fire at, the game informs the user if the shot hit or missed, as well as the total number of shots remaining. 

![Results Page Image](./assets/images/results-page.png)

* Game Over - After all shots have been fired or all ships have been sunk, the game ends.

![Results Page Image](./assets/images/results-page.png)

## Features Left to Implement
* A future feature I would like to add is an option for the user to select the position of their own ships on the grid, as well as the size of the game grid.

## Testing
*  This project passed through PEP8 with no issues returned.

![PEP8 Testing Image](./assets/images/PEP8.png)

### Bugs
* When creating the difficulty setting, the 'Difficult Mode' didn't work. It would default to 'Easy Mode' despite the number 2 being selected. This was due to a typo on line 89, the number was '1' from the copy/paste of the 'Easy Mode' not being corrected. 

### Unfixed Bugs

## Deployment
1. This site was deployed to Heroku. 
* Create a fork or a clone of the 'Battleship" repository.
* Go to the Heroku page, and create a new app.
* When selecting the buildbacks, choose python and NodeJS, in that order.
* Link the create Heroku app to the "Battleship" repository.
* Select 'Deploy'.

### How to make a clone
* While in your repository, click the code button.
* You will have three options, Clone, Download or Open with Github Desktop. 
* Clone the repository using HTTPS by clicking on the copy button. Then copy the given URL.
* You can then either launch the Gitpod workspace or choose your own directory.
* Open Git Bash.
* Type git clone and then paste the URL of the cloned repository.
* Press Enter, to create your local clone to your chosen directory.

## Credits and Acknowledgements

1. Code Institute and the Love Sandwiches walkthrough.

2. Youtube: "How to Code Battleship in Python - Single Player Game" by Knowledge Mavens, and the creators' associated GitHub, Garrett Broughton.

3. Pythondex - Python Battleship Game

4. The reddit community "r/learnpython" for tips and considerations.

5. Geeks for Geeks 

6. Stack Overflow.

7. My lovely wife for help with the difficulty function.