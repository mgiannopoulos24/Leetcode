class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_place(row, col):
            # Check column
            if col_used[col]:
                return False
            # Check upleft diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r] == c:
                    return False
                r -= 1
                c -= 1
            # Check upright diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r] == c:
                    return False
                r -= 1
                c += 1
            return True
        
        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if can_place(row, col):
                    board[row] = col
                    col_used[col] = True
                    backtrack(row + 1)
                    col_used[col] = False
                    board[row] = -1
        
        count = 0
        board = [-1] * n
        col_used = [False] * n
        backtrack(0)
        return count
