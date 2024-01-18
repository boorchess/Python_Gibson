import random

def roll_dice(num_sides=6):
    """Roll a single die with a given number of sides."""
    return random.randint(1, num_sides)

def dice_game():
    """Simple dice game where two players roll a die each and the highest roll wins."""
    num_sides = 6  # Standard six-sided dice

    player1_roll = roll_dice(num_sides)
    player2_roll = roll_dice(num_sides)

    print(f"Player 1 rolled: {player1_roll}")
    print(f"Player 2 rolled: {player2_roll}")

    if player1_roll > player2_roll:
        print("Player 1 wins!")
    elif player2_roll > player1_roll:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Running the game
dice_game()
