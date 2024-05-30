from flask import Flask, request, render_template, redirect, url_for
from typing import List
import json

app = Flask(__name__)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
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

        res = []
        for i in range(n):
            if board[i][0] == 'O':
                res.append((i, 0))
            if board[i][m - 1] == 'O':
                res.append((i, m - 1))

        for j in range(1, m - 1):
            if board[0][j] == 'O':
                res.append((0, j))
            if board[n - 1][j] == 'O':
                res.append((n - 1, j))

        if len(res) == 0:
            for i in range(n):
                for j in range(m):
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

                            if 0 <= n_row < n and 0 <= n_col < m and (n_row, n_col) not in visited:
                                if board[n_row][n_col] == 'O':
                                    queue.append((n_row, n_col))
                                    visited[(n_row, n_col)] = True

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'I':
                    board[i][j] = 'O'

        return board


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            board_input = request.form['board']
            board = json.loads(board_input)
            solution = Solution()
            solved_board = solution.solve(board)
            return render_template('index.html', original_board=board_input, solved_board=solved_board)
        except ValueError as exception:
            return render_template('index.html', error=str(exception))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
