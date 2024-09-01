from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        def countLiveNeighbors(x, y):
            live_count = 0
            for i in range(max(0, x - 1), min(m, x + 2)):
                for j in range(max(0, y - 1), min(n, y + 2)):
                    if (i != x or j != y) and board[i][j] & 1 == 1:
                        live_count += 1
            return live_count
        
        # Iterate over each cell to determine the next state
        for i in range(m):
            for j in range(n):
                live_neighbors = countLiveNeighbors(i, j)
                if board[i][j] & 1 == 1:
                    # Current cell is live
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 1  # Mark as dying in the future
                    else:
                        board[i][j] = 3  # Mark as living in the future
                else:
                    # Current cell is dead
                    if live_neighbors == 3:
                        board[i][j] = 2  # Mark as coming to life in the future
        
        # Decode the board
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1  # Shift to get the new state
    
