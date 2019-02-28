import random

def roll_dice():
    return random.randint(1, 6)

class ComputerPlayer:
    """
    Computer oppoenent in the game of Pig. Rolls die until either 20 points or a 1 is rolled.
    """
    def roll_die(self):
        computerscore = 0
        while computerscore < 20:
            roll = roll_dice()
            if roll != 1:
                computerscore += roll
                print(f"The computer rolled a {roll}")
            else:
                print(f"The computer rolled a 1.")
                computerscore = 0
                break
        print(f"\nComputer turn is over, it scored {computerscore} for this round.")
        return computerscore

class HumanPlayer:
    """
    Human player who choses to either roll or hold
    """
    def roll_die(self):
        playerscore = 0
        roll_hold_option = "y"
        while roll_hold_option.strip().casefold() == "y":
            roll = roll_dice()
            if roll != 1:
                playerscore += roll
                print(f"\nYou rolled a {roll}, your current score for this round is {playerscore}")
                roll_hold_option = input("Would you like to roll again (y/n): ")
            elif roll == 1:
                print(f"\nUh-oh you rolled a 1!")
                playerscore = 0
                break
        print(f"\nYour turn is over, your score for this round is {playerscore}.")
        return playerscore

if __name__ == "__main__":
    
    computer = ComputerPlayer()
    player = HumanPlayer()

    print(computer.roll_die())
    print(player.roll_die())



 