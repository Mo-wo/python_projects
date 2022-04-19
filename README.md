# ease_it
My part of the ease_it web application (https://ease-it-app.netlify.app/) for Side Hustle Internship Boot Camp

Rock-Paper-Scissors Game
Getting started
Here are some steps to get you started in the Rock Paper Scissors project! As you work through the project, make sure to test your program by running it.

1. Check out the starter code
You can find all of the starter code in the workspace on the following page. Or if you prefer to work on the project in your own code editor, you can download a copy of the starter code here.

The starter code gives you a place to begin, with Player and Game classes that are mostly empty. Over the course of the project, you will be greatly expanding the classes and methods in this program.

Read the starter code, and run it on your computer to see what it does.

Try importing it into the Python interpreter and experimenting with the Player and Game objects.

2. Create a player subclass that plays randomly
The starter Player class always plays 'rock'. That's not a very good strategy! Create a subclass called RandomPlayer that chooses its move at random. When you call the move method on a RandomPlayer object, it should return one of 'rock', 'paper', or 'scissors' at random.

Change the code so it plays a game between two RandomPlayer objects.

3. Keep score
The starter Game class does not keep score. It doesn't even notice which player won each round. Update the Game class so that it displays the outcome of each round, and keeps score for both players. You can use the provided beats function, which tells whether one move beats another one.

Make sure to handle ties — when both players make the same move!

4. Create a subclass for a human player.
The game is a lot more interesting if you can actually play it, instead of just watching the computer play against itself. Create a HumanPlayer subclass, whose move method asks the human user what move to make. (Take another look back at the project demo to see what this can look like!)

Set the program to play a game between HumanPlayer and RandomPlayer.

5. Create player classes that remember
At the end of each game round, the Game class calls the learn method on each player object, to tell that player what the other player's move was. This means you can have computer players that change their moves depending on what has happened earlier in the game. To do this, you will need to implement learn methods that save information into instance variables.

Create a ReflectPlayer class that remembers what move the opponent played last round, and plays that move this round. (In other words, if you play 'paper' on the first round, a ReflectPlayer will play 'paper' on the second round.)

Create a CyclePlayer class that remembers what move it played last round, and cycles through the different moves. (If it played 'rock' this round, it should play 'paper' in the next round.)

(Something to think about: What should these classes do on the first move?)

Test each of these player classes versus HumanPlayer.

6. Validate user input
The human player might sometimes make typos. If they enter roxk instead of rock, the HumanPlayer code should let them try again. (See how this works in the demo if you type something in that isn't a valid move.)

7. Announce the winner
It's up to you how long the game should run. The starter code always plays three rounds, but that's not the only way it could work. You could choose to continue until the player types quit, or you could have the game run until one player is ahead by three points, or any other rule that makes sense to you.

At the end of the game, have it print out which player won, and what the final scores are.

8. Check your code formatting
Use the pycodestyle tool to check the formatting of your code. Make the edits that it recommends, then re-run it to see fewer and fewer warnings. By the time you're done, it should display no warnings or errors at all.

PROJECT SPECIFICATION
Rock Paper Scissors

Gameplay

CRITERIA
MEETS SPECIFICATIONS
1 The program plays a game of Rock Paper Scissors, following the conventional rules.

Paper beats rock; rock beats scissors; scissors beat paper.

2. The program plays a match consisting of multiple rounds, and tracks players' total score.

The game displays the results after each round, including each player's score. At the end, the final score is displayed.
The number of rounds per game, as well as when to stop, are up to you!

3. There are at least four different computer player classes, each implementing a different strategy.

The game should have (at least) four computer player strategies:

A player that always plays 'rock'
A player that chooses its moves randomly.
A player that remembers and imitates what the human player did in the previous round.
A player that cycles through the three moves

4. Each player class has a method that returns that player's move, and a method for remembering information about the round.

The game should call each player's move method once in each round, to get that player's move. After each round, it should call the remembering method to tell each player what the other player's move was.

Some computer players don't need to remember anything, so their remembering method should do nothing.

*Object-Oriented Programming*

CRITERIA
MEETS SPECIFICATIONS
1. The code uses classes and objects to store game data, rather than global variables.

The Game class should include a method to play a single round, and a method to play a match of several rounds.

Facts about the current match, such as the players' score, or the number of rounds played, should be stored as instance variables. They shouldn't be stored as global variables.

It's okay to use global variables for the game moves "rock", "paper", and "scissors".

2. The code uses subclasses appropriately.

Each computer player strategy should be a subclass of the Player base class, as should the Human player.

Code Style

CRITERIA
MEETS SPECIFICATIONS
1. The code style follows the standard Python style guide.

The pycodestyle tool should report zero errors and zero warnings.

If the program is called rps.py, the command to test it is pycodestyle rps.py.

2. The program does not crash or display any error messages.

The code should be thoroughly tested.

Invalid moves should not make the program crash. (See the next item!)

3. The program checks the validity of user input.

If the player enters a move that is not valid, the game should give them the chance to retry that move until they enter a valid move.

The game should not crash, and it should not treat invalid input as a valid move.

Example:
If the player enters "roxk" instead of "rock", the game should let them try again; it should not crash, and it should not assume they meant "rock".

Suggestions to Make Your Project Stand Out!
Adapting the game to play Rock Paper Scissors Spock Lizard or another expanded version of the game.
Running a tournament of many computer players, with different strategies, and discovering which strategies win the most!
Adding color or other features to the game display. (Look up "terminal color codes" in your favorite search engine.)