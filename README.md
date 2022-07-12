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

#### Grid and Ship size
* I chose to implement a 8x8 grid size for this game because I feel it is a large enough map to make the game difficult without being impossible to find opponent ships. 
* I chose to have ships as a 1x1 square size and positioned randomly on the board to have a true random game setup.
* If the user chooses a shot location not on the grid, the game informs them the coordinates are not valid and to try again.

## Features

* Randomized ship locations on playing board.
* Validated user input for shot coordinates - checks initial shots and also for duplicate shot locations. If the chosen point is not on the grid, the game tells the user to input a valid position. If the user fires on a duplicate location, the game tells the user this has already been used and to choose a new set of coordinates.
* Informs the user if the selected coordinates are a hit or miss. 
* Informs user the number of shots remaining.
* Informs the user the game is over, either with no remaining shots or that all ships have been destroyed.

* Starting Screen - The game initializes

![Starting image](./assets/images/starting-image.png)

* Game Page - Asks the user to input a set of coordinates to fire on the game board.

![Game Image](./assets/images/game-image.png)

* Results - After selecting a row and column to fire at, the game informs the user if the shot hit or missed, as well as the total number of shots remaining. 

![Results Page Image](./assets/images/results-page.png)

## Features Left to Implement
* A future feature I would like to add is an option for the user to select the position of their own ships on the grid, as well as the size of the game grid.

## Testing
* This project was primarily built in Google Chrome but also in Firefox. It was tested in Microsoft Edge, Firefox and Safari browsers. 
* The 'Play', 'Submit', and 'Reload' buttons all work as intended, moving to the next page or question.
* When running Lighthouse for Desktop, the SEO comes back limited due to links not being crawlable. But the links are from third parties and not from my own code. 
* When running Lighthouse for Mobile, the performance was limited but was remedied by removing the fontawesome script from the index and game html files. 

* Lighthouse Desktop - Index Page

![Lighthouse Desktop Index Image](./assets/images/lighthouse-index-desktop.png)

* Lighthouse Desktop - Game Page

![Lighthouse Desktop Game Image](./assets/images/lighthouse-game-desktop.png)

* Lighthouse Mobile - Index Page

![Lighthouse Mobile Index Image](./assets/images/lighthouse-index-mobile.png)

* Lighthouse Mobile - Game Page

![Lighthouse Mobile Game Image](./assets/images/lighthouse-game-mobile.png)

### Validator Testing
HTML
* No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fchristianlund2.github.io%2Fvery-varied-quiz%2Fgame.html).

JavaScript 
* When run through JShint I had a lot of missing semi-colons. There were variables that I named or intended to use when wireframing that were not used and later removed. JShint was also giving me warnings when I used const for variables, this was fixed by adding '/*jshint esversion: 6 */' to the top of my js file. 

Python

### Unfixed Bugs
* Unfixed bugs go here

## Deployment
1. This site was deployed to GitHub pages. 
* In the "battleship" repository, click on the "Settings" tab.
* Under "Code and Automation", select the "Pages" section.
* Under Source, change from "Branch: None" to "Branch: Main" and click "Save".
* After a few minutes, a banner appears confirming the site is published with a live link. 

### How to make a clone
* While in your repository, click the code button.
* You will have three options, Clone, Download or Open with Github Desktop. 
* Clone the repository using HTTPS by clicking on the copy button. Then copy the given URL.
* You can then either launch the Gitpod workspace or choose your own directory.
* Open Git Bash.
* Type git clone and then paste the URL of the cloned repository.
* Press Enter, to create your local clone to your chosen directory.

## Credits

1. Love Maths Project - An obvious help. Although I didn't make a game, the foundations were very helpful. 

2. Youtube: Web Dev Simplified - "Build a Quiz App with Javascript" - This was a great resource for this project. I went through this video multiple times. Great for starting with the basics.