Pig

Contents:
2 Players (1 human, 1 computer)
1 Die
Scoresheet

Rules:
The goal is to be the first player to reach or exceed 100 points.  Points are awarded by the numerical value of the die roll for 2-6.  If a 1 is rolled that players turn is over and no points are awarded.  

One player starts by rolling the die.  As long as the player does not roll a 1, they can either choose to hold and take the points of their die value, or they can roll again.  The player will continue to accumulate the points of their rolls until either they hold or roll a 1.  Rolling a 1 negates all prior points accumulated by the player in that turn, so choose carefully!

The first player to reach or exceed 100 points wins.

Areas to Program:

Computer_player: always holds until they reach 20 points or a 1 is rolled

Human_player: need the option to choose either hold or roll-again unless a 1 is rolled, then turn is automatically over.  Some type of while loop (while die != 1) looking for input to hold or roll_again

Scoresheet: needs to compile each players score and check to see when a player wins i.e. when either player’s score is not >= 100

Die: needs to randomly generate a number between 1 - 6 to mimic die roll

Potential Classes:

pig_game 
HumanPlayer —> action_input (roll, hold), total_score (value of all turns up to date) —> scoresheet
CompPlayer —> action (hold until 20), total_score (value of all turns up to date) —> scoresheet
ScoreSheet —> value of roll, score per turn (i.e. adding value of rolls until hold, 20+ points for comp, or 1 is rolled and no points assigned) —> will work with players and scoresheet

Where to Start?

Build a dice class and test that it returns a random value between 1-6. Test

Build out option to hold or roll again based on user input or logic in computer’s case
