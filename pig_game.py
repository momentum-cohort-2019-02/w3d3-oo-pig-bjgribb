import random

# Need option to play again
# Not much error handling for incorrect inputs throughout (i.e. roll again for HumanPlayer)
# Game could randomize assignment of starting player


def roll_dice():
    return random.randint(1, 6)

class ComputerPlayer:
    """
    Computer oppoenent in the game of Pig. Rolls die until either 20 points or a 1 is rolled.  Compiles score for current turn.
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

    def announce_win(self, computer_score):
        if computer_score >= 100:
            print(f"You lose.")
            return True

class HumanPlayer:
    """
    Human player who choses to either roll or hold and this compiles their score for current turn.
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

    def announce_win(self, player_score):
        if player_score >= 100:
            print(f"You're the winner!!")

        

class PigGame:
    """Runs through the game with the two participants, computer and human player"""
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def pig_summary(self, player_score, computer_score):
        print(f"""Thanks for playing! Still working on the play again feature...
        \nComputer: {computer_score} You: {player_score}""")


    def run_pig(self):
        player_score = 0
        computer_score = 0

        print(f"Welcome to the game of Pig. It's you versus the computer. Your roll starts automatically.")

        while player_score < 100 and computer_score < 100:
            if computer_score >= 100:
                break
            else:
                player_score += HumanPlayer.roll_die(self)
                print(f"Your total score is {player_score}.\n")
            if player_score >= 100:
                break
            else:
                computer_score += ComputerPlayer.roll_die(self)
                print(f"The computer's total score is {computer_score}.\n")

        if player_score > computer_score:
            self.player.announce_win(player_score)
        else:
            self.computer.announce_win(computer_score)

        self.pig_summary(player_score, computer_score)



if __name__ == "__main__":
    
    computer = ComputerPlayer()
    player = HumanPlayer()

    pig_game = PigGame(player, computer)

    pig_game.run_pig()


 