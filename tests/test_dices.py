from model.dices import roll 

def test_roll_single_die():
    result = roll()  # Default to a single 6-sided die
    assert 1 <= result <= 6  # Check if the result is within the expected range

def test_roll_multiple_dice():
    result = roll(die=10, number_of_dice=3)  # Roll three 10-sided dice 
    assert 3 <= result <= 30 
