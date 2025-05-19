# May 2025 Python Programming Skill Assessment Project
# Tic-Tac-Toe Game

# Important Modules
import random

def main():
    intro()
    player_symbol, computer_symbol = player_symbols()
    board = [" " for _ in range(9)]
    display_board(board)
    play_game(player_symbol, computer_symbol, board)


def intro():
    # Welcome Message and Game Introduction
    welcome_message = """
    ----------------------------------------
    ::: Welcome to the Tic-Tac-Toe Game! :::
    ----------------------------------------
    Here are the rules:
    
    - Player 01 and Player 02, represented by X and O,
      take turns marking spaces on a 3x3 grid. 
      
    - The player who succeeds at placing three of their 
      symbols in a horizontal, vertical, or diagonal row wins.
    
    - X always goes first, then O.
    - A stalemate is when no moves remain.
    """
    print(welcome_message)
    input("Please press enter to start:")


# Determine player symbol and turn order
def player_symbols():
    print("\nBefore we continue, let's determine who will go first.\n")
    player_symbol = input("Would you like to be X or O?: ").strip().upper()
    while player_symbol not in ("X", "O"):
        print("Invalid input. Please choose X or O.")
        player_symbol = input("Would you like to be X or O?: ").strip().upper()

    computer_symbol = "O" if player_symbol == "X" else "X"
    print(f"The computer will be {computer_symbol}.")
    return player_symbol, computer_symbol


def display_board(board):
    # Display Game Board
    display = [str(i + 1) if space == " " else space for i, space in enumerate(board)]
    print()
    print(f" {display[0]} | {display[1]} | {display[2]}")
    print("---+---+---")
    print(f" {display[3]} | {display[4]} | {display[5]}")
    print("---+---+---")
    print(f" {display[6]} | {display[7]} | {display[8]}")
    print()


def get_player_move(board):
    while True:
        user_input = input("Please select an empty section on the grid (1-9): ")
        try:
            move = int(user_input)
            if not 1 <= move <= 9:
                print("Invalid input. Please choose a number between 1 and 9.")
                continue
            if board[move - 1] != " ":
                print("That spot is already taken. Please choose another cell.")
                continue
            return move - 1 # Returns index for board
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")



def get_computer_move(board):
    available_moves = [i for i, space in enumerate(board) if space == " "]
    return random.choice(available_moves)


def check_winner(board, symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6],            # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == symbol for i in combo):
            return True
    return False


def play_game(player_symbol, computer_symbol, board):
    current_symbol = "X" # X always goes first
    while True:
        if current_symbol == player_symbol:
            print("Your turn:")
            move = get_player_move(board)
        else:
            print("Computer's turn:")
            move = get_computer_move(board)

        board[move] = current_symbol
        display_board(board)

        if check_winner(board, current_symbol):
            if current_symbol == player_symbol:
                print("Congratulations! You win!")
            else:
                print("Computer wins! Better luck next time.")
            break

        if " " not in board:
            print("It's a stalemate!")
            break

        # Switch turns
        current_symbol = computer_symbol if current_symbol == player_symbol else player_symbol


# Main loop for playing a new game
if __name__ == "__main__":
    while True:
        main()

        # Ask if the user would like to play an additional round
        play_again = input("\nWould you like to play another game? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! See you next time.")
            break

