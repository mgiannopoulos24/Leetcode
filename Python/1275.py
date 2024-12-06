class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize a 3x3 grid
        grid = [[''] * 3 for _ in range(3)]
        
        # Process moves, players A ('X') and B ('O')
        for i, move in enumerate(moves):
            row, col = move
            if i % 2 == 0:  # Player A's turn (even index)
                grid[row][col] = 'X'
            else:           # Player B's turn (odd index)
                grid[row][col] = 'O'
            
            # After each move, check if the current player has won
            if self.isWinner(grid, row, col):
                return 'A' if i % 2 == 0 else 'B'
        
        # If all moves have been played and no winner, check if it's a draw
        if len(moves) == 9:
            return "Draw"
        
        # Otherwise, the game is still pending
        return "Pending"
    
    # Helper function to check if a player has won
    def isWinner(self, grid: List[List[str]], row: int, col: int) -> bool:
        player = grid[row][col]
        
        # Check the row
        if all(grid[row][j] == player for j in range(3)):
            return True
        
        # Check the column
        if all(grid[i][col] == player for i in range(3)):
            return True
        
        # Check the main diagonal
        if row == col and all(grid[i][i] == player for i in range(3)):
            return True
        
        # Check the anti-diagonal
        if row + col == 2 and all(grid[i][2-i] == player for i in range(3)):
            return True
        
        return False
