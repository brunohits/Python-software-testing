from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            raise ValueError("Board cannot be empty")

        n, m = len(board), len(board[0])
        if not (1 <= n <= 200) or not (1 <= m <= 200):
            raise ValueError("Invalid board size")

        for row in board:
            if len(row) != m:
                raise ValueError("Invalid board shape")
            if any(cell not in {'X', 'O'} for cell in row):
                raise ValueError("Invalid character in board")

        m = len(board)
        n = len(board[0])

        res = []
        for i in range(m):
            if board[i][0] == 'O':
                res.append((i, 0))
            if board[i][n - 1] == 'O':
                res.append((i, n - 1))

        for j in range(1, n - 1):
            if board[0][j] == 'O':
                res.append((0, j))
            if board[m - 1][j] == 'O':
                res.append((m - 1, j))

        if len(res) == 0:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
            return board

        visited = {}
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if len(res) > 0:
            for pair in res:
                if (pair[0], pair[1]) not in visited:
                    queue = []
                    queue.append((pair[0], pair[1]))
                    visited[(pair[0], pair[1])] = True

                    while len(queue) > 0:
                        row, col = queue.pop(0)

                        board[row][col] = 'I'
                        for x in directions:
                            n_row = row + x[0]
                            n_col = col + x[1]

                            if 0 <= n_row < m and 0 <= n_col < n and (n_row, n_col) not in visited:
                                if board[n_row][n_col] == 'O':
                                    queue.append((n_row, n_col))
                                    visited[(n_row, n_col)] = True

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'I':
                    board[i][j] = 'O'

        return board





