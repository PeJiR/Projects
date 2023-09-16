import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Import the functions from the tic-tac-toe code.
from tic_tac_toe import tic_tac_toe, print_board, get_move, check_winner, is_full

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.board = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['O', 'X', 'X']]

    def test_print_board(self):
        expected_output = "X O X\nO X O\nO X X\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        print_board(self.board)
        sys.stdout = sys.__stdout__  # Reset the sys.stdout
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["1 1", "1 2", "2 1", "2 2", "3 1"])
    def test_get_move(self, mock_input):
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]

        expected_moves = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
        for move in expected_moves:
            row, col = get_move('X', "Player", board)
            self.assertEqual((row, col), move)

    def test_check_winner(self):
        self.assertEqual(check_winner(self.board), 'X')

    def test_is_full(self):
        full_board = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['O', 'X', 'X']]
        self.assertTrue(is_full(full_board))

        partial_board = [['X', 'O', 'X'],
                         ['O', 'X', ' '],
                         ['O', 'X', 'X']]
        self.assertFalse(is_full(partial_board))

if __name__ == '__main__':
    unittest.main()
