import unittest

from Task_1.solution import Solution


class TestSolution(unittest.TestCase):
    def test_leetcode_case_1(self):
        sut = Solution()
        self.assertEqual(
            sut.solve([["X", "X", "X", "X"],
                       ["X", "O", "O", "X"],
                       ["X", "X", "O", "X"],
                       ["X", "O", "X", "X"]]),
            [["X", "X", "X", "X"],
             ["X", "X", "X", "X"],
             ["X", "X", "X", "X"],
             ["X", "O", "X", "X"]])

    def test_leetcode_case_2(self):
        sut = Solution()
        self.assertEqual(
            sut.solve([["X"]]),
            [["X"]])

    def test_all_O(self):
        sut = Solution()
        self.assertEqual(sut.solve([["O", "O"],
                                    ["O", "O"]]),
                         [["O", "O"],
                          ["O", "O"]])

    def test_0_in_center(self):
        sut = Solution()
        self.assertEqual(sut.solve([["X", "X", "X"],
                                    ["X", "O", "X"],
                                    ["X", "X", "X"]]),
                         [["X", "X", "X"],
                          ["X", "X", "X"],
                          ["X", "X", "X"]])

    def test_borders_are_O(self):
        sut = Solution()
        self.assertEqual(sut.solve([["O", "X", "O"],
                                    ["X", "O", "X"],
                                    ["O", "X", "O"]]),
                         [["O", "X", "O"],
                          ["X", "X", "X"],
                          ["O", "X", "O"]])

    def test_large_board(self):
        sut = Solution()
        board = [
            ["X"] * 200 for _ in range(200)
        ]
        board[0][0] = "O"
        board[199][199] = "O"
        expected = [
            ["X"] * 200 for _ in range(200)
        ]
        expected[0][0] = "O"
        expected[199][199] = "O"
        self.assertEqual(sut.solve(board), expected)

    def test_invalid_sizes(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.solve([])

        with self.assertRaises(ValueError):
            sut.solve([["X"] * 201 for _ in range(201)])

    def test_invalid_characters(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.solve([
                ["X", "Z"],
                ["SXL", "123"]])


if __name__ == '__main__':
    unittest.main()
