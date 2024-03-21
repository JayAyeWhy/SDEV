"""
arrays_program2.py

This Python program is a simple game where the player has to guess the position of a ship on a board. 
The board size is determined at the start of the game. 
The player takes turns guessing the ship's position. 
After each guess, the board is displayed with the positions the player has guessed so far. 
The game continues until the player guesses the ship's position correctly.
"""
import random

def display_board(board_size: int, guessed_positions: list[int],
                  ship_position: int) -> None:

    for i in range(0,board_size,1):
        found = False
        for j in range(0,len(guessed_positions),1):
            if i+1 == guessed_positions[j]:
                if guessed_positions[j] == ship_position:
                    print(" X |", end="")
                else:
                    print(" O |", end="")
                found = True
                break
        if not found:
            print(" . |", end="")
    print ("\n", end="")
    for i in range(0,board_size,1):
        print(" " + str(i+1) + " |", end="")
    if guessed_positions == []:
        print("")

    pass

def get_board_size() -> int:
    # Print an appropriate message and get the board size from the user.
    size = int(input("Enter the board size: "))
    return size

def get_guess() -> int:
    guess = input("Enter your guess:  ")
    # Print an appropriate message and get a guess from the user.
    return guess
  
def is_hit(guess: int, ship_position: int) -> bool:
    if guess == ship_position:
        return True
    else:
        return False
    # Return whether the guess hit the target

def initialize_ship_position(board_size: int) -> int:
    ShipPosition = random.randint(0, board_size)
    return ShipPosition

def print_hit_message(is_hit: bool) -> None:
    if is_hit:
        print("\n" + "Hit! You sank the ship!")
    else:
        print("\n" + "Missed")
    # Print hit or miss message.
    pass

def take_turn(board_size: int, guessed_positions: list[int],
              ship_position: int) -> bool:
    booleen = False
    guess = int(get_guess())
    guessed_positions.append(int(guess))
    display_board(board_size,guessed_positions,ship_position)
    if guess == ship_position:
        print_hit_message(True)
        booleen = True
    else:
        print_hit_message(False)
    # Return whether the battleship was hit.
    return booleen
    

def main():
    print("Welcome to Battleship!")

    # TODO: Uncomment these one at a time and complete.
    board_size: int = get_board_size()
    ship_position: int = initialize_ship_position(board_size)
    guessed_positions: list[int] = []
    display_board(board_size, guessed_positions, ship_position)
    booleen = False
    while booleen == False:
        booleen = take_turn(board_size, guessed_positions, ship_position)
        
if __name__ == "__main__":
    main()

