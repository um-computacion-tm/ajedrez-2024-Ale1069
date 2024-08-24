import unittest 
from pieces import Rook
from board import Board

class TestBoard(unittest.TestCase):

    def test_initial_setup(self):
        board = Board()

        # Verifica las posiciones iniciales de las torres negras
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertEqual(str(board.get_piece(0, 0)), "\u265c")  # Torre negra
        self.assertIsInstance(board.get_piece(0, 7), Rook)
        self.assertEqual(str(board.get_piece(0, 7)), "\u265c")  # Torre negra

        # Verifica las posiciones iniciales de las torres blancas
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertEqual(str(board.get_piece(7, 0)), "\u2656")  # Torre blanca
        self.assertIsInstance(board.get_piece(7, 7), Rook)
        self.assertEqual(str(board.get_piece(7, 7)), "\u2656")  # Torre blanca

if __name__ == '__main__':
    unittest.main()