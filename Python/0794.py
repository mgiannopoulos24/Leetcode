class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def check_win(player: str) -> bool:
            # Check rows, columns, and diagonals for a win
            return (any(all(cell == player for cell in board[i]) for i in range(3)) or
                    any(all(board[i][j] == player for i in range(3)) for j in range(3)) or
                    all(board[i][i] == player for i in range(3)) or
                    all(board[i][2 - i] == player for i in range(3)))

        count_X = sum(row.count('X') for row in board)
        count_O = sum(row.count('O') for row in board)
        
        # Check if the counts are valid
        if count_X != count_O and count_X != count_O + 1:
            return False
        
        x_wins = check_win('X')
        o_wins = check_win('O')
        
        # Both players cannot win simultaneously
        if x_wins and o_wins:
            return False
        
        # If X wins, X should have exactly one more than O
        if x_wins and count_X != count_O + 1:
            return False
        
        # If O wins, O should have the same count as X
        if o_wins and count_X != count_O:
            return False
        
        return True