# Tic-Tac-Toe Game

Welcome to the Tic Tac Toe Game. Players will take turns marking spaces in a 3x3 grid with their chosen symbol. The objective is to be the first to get three of their marks in a row, horizontally, vertically, or diagonally. If neither player achieves three-in-a-row, the game ends in a stalemate (also called a 'cat's game' or a 'cat's meow'). 

---

## Features
- Play as **X** or **O**
- Turn-based logic where **X always goes first**
- Intelligent computer opponent (randomized move selection)
- Win/Tie Detection
- Input validation with helpful prompts
- Option to play multiple rounds
- Fully tested with unittest


---

## How to Play

1. Run the script in a Python Interpreter:
```bash
python Tic_Tac_Toe_Game.py
```
2. Select which symbol you would like to be (remember that **X** goes first).
3. Make your move by selecting a number between 1-9. Note: Players will take turns placing their marks on empty spaces.
4. The first player to get three-in-a-row (horizontally, vertically, or diagonally) wins!
5. If all spaces are filled and no player has three-in-a-row, the game is a stalemate.

---

## Requirements

- Python 3.x
- No additional libraries are required as the game relies on the standard Python Library.

---

## Example Gameplay

```
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
    
Please press enter to start:

Before we continue, let's determine who will go first.

Would you like to be X or O?: x
The computer will be O.

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Your turn:
Please select an empty section on the grid (1-9): 5

 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

Computer's turn:

 1 | 2 | O
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

Your turn:
Please select an empty section on the grid (1-9):
```

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HomeBase85/Tic_Tac_Toe_Game.git
cd Tic_Tac_Toe_Game-cli
```

## Acknowledgements

This project was created as a fun programming exercise to practice Python fundamentals and game logic development. Feel free to contribute, provide feedback, or use the code for your own projects!

---

## License

This project is open-source and free to use under the MIT License. Contributions and improvements are welcome!