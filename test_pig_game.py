from pig_game import roll_dice, ComputerPlayer

def test_roll_dice():
    assert roll_dice() in [1, 2, 3, 4, 5, 6]

def test_comp_roll_die():
    computer = ComputerPlayer()
    computerscore = computer.roll_die()
    assert computerscore == 0 or computerscore >= 20
    assert computerscore not in range(1,21)






