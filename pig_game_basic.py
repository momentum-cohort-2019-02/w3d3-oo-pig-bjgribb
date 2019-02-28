import random

def roll_dice():
    return random.randint(1, 6)

def player_move():
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

def computer_move():
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

def pig_winner(total_playerscore, total_computerscore):
    if total_playerscore > total_computerscore:
        print(f"You're the winner!! You scored {total_playerscore} vs the computer's {total_computerscore}!")
    else:
        print(f"You lose. Computer: {total_computerscore} You: {total_playerscore}")
    

def game_of_pig(computer_move, player_move):
    total_playerscore = 0
    total_computerscore = 0

    print(f"Welcome to the game of Pig. It's you versus the computer.")

    while total_playerscore < 100 and total_computerscore < 100:
        
        total_playerscore += player_move()
        print(f"Your total score is {total_playerscore}.\n")

        total_computerscore += computer_move()
        print(f"The computer's total score is {total_computerscore}.\n")
    
    pig_winner(total_playerscore, total_computerscore)

if __name__ == "__main__":
    game_of_pig(computer_move, player_move)
