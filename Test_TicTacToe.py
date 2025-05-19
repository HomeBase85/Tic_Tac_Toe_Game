import unittest
from Tic_Tac_Toe_Game import (
    player_symbols,
    display_board,
    get_player_move,
    get_computer_move,
    check_winner
)

from unittest.mock import patch
import builtins

class TestTicTacToe(unittest.TestCase):

    def test_check_winner_true(self):
        board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        self.assertFalse(check_winner(board, "X"))

    def test_get_computer_move_returns_valid_index(self):
        board = ["X", "O", "X", " ", " ", " ", " ", " ", " "]
        move = get_computer_move(board)
        self.assertIn(move, [i for i, cell in enumerate(board) if cell == " "])

    @patch("builtins.input", side_effect=["5"])
    def test_get_player_move_valid(self, mock_input):
        board = [" "] * 9
        move = get_player_move(board)
        self.assertEqual(move, 4)

    @patch("builtins.input", side_effect=["0", "10", "abc", "3"])
    def test_get_player_move_invalid_then_valid(self, mock_input):
        board = [" "] * 9
        move = get_player_move(board)
        self.assertEqual(move, 2)

    @patch("builtins.input", side_effect=["X"])
    def test_player_symbols_x(self, mock_input):
        with patch("builtins.print"):
            player, computer = player_symbols()
        self.assertEqual(player, "X")
        self.assertEqual(computer, "O")

    @patch("builtins.input", side_effect=["z", "o"])
    def test_player_symbols_invalid_then_valid(self, mock_input):
        with patch("builtins.print"):
            player, computer = player_symbols()
        self.assertEqual(player, "O")
        self.assertEqual(computer, "X")

if __name__ == "__main__":
    unittest.main()