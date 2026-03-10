import unittest
from src.eight_queens import count_n_queens, solve_n_queens

class TestEightQueens(unittest.TestCase):
    def test_4_queens(self):
        self.assertEqual(count_n_queens(4), 2)

    def test_8_queens(self):
        self.assertEqual(count_n_queens(8), 92)

if __name__ == '__main__':
    unittest.main()
