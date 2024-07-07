from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_place(row, col):
            # Check column
            for r in range(row):
                if board[r][col] == 'Q':
                    return False
            # Check upleft diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            # Check upright diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1
            return True
        
        def backtrack(row):
            nonlocal solutions
            if row == n:
                solutions.append(list(board))
                return
            for col in range(n):
                if can_place(row, col):
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                    backtrack(row + 1)
                    board[row] = board[row][:col] + '.' + board[row][col+1:]
        
        solutions = []
        board = ['.' * n for _ in range(n)]
        backtrack(0)
        return [[''.join(row) for row in solution] for solution in solutions]
