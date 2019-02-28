import random

class Scoresheet:
    """Roll die and return value, option for player to hold or roll again, ends when 1 is rolled, otherwise compiles rolls for turn score."""

    def roll_die(self):
        """Randomly picks a number between 1 and 6 and lets user know value."""
        die_value = random.randint(1, 6)
        if die_value != 1:
            print(f"You've rolled a {die_value}.")
            return int(die_value)
        else:
            print(f"Uh-oh, you rolled a 1, no points for you.")
            return 0

    def roll_again(self):
        """allows player to select if they would like to roll again or hold"""
        roll_option = input("Would you like to roll again (y/n): ")
        if roll_option.casefold().strip() == "y":
            return True
        else:
            return False

    def turn_score(self):
        """As long as the player is choosing to roll again and doesn't roll a 1, compile the score"""
        # turn.roll_die()
        # turn.roll_again()
        turn_score = 0
        while turn.roll_again() == True:
            single_roll_score = turn.roll_die()
            single_roll_score += turn_score
            return turn_score


class Player:
    """This is the human player, responsiblity to compile turn scores from scoresheet"""

class Computer:
    """This is the computer player, responsiblity to compile turn scores from scoresheet"""

class Pig:
    """This is the main game and will initiate and run thru the game of Pig. Calls out winner when player reaches 100+ points."""
    pass

if __name__ == "__main__":
    
    turn = Scoresheet()

    turn.roll_die()




 