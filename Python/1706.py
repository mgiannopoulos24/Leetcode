from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        def drop_ball(col: int) -> int:
            for row in range(m):
                direction = grid[row][col]
                next_col = col + direction  # Calculate the next column based on direction
                
                # Check if the ball is stuck in a "V" shape or hits a wall
                if next_col < 0 or next_col >= n or grid[row][next_col] != direction:
                    return -1  # Ball is stuck, return -1
                
                # Move to the next column
                col = next_col
                
            return col  # Ball falls out of the grid at column `col`
        
        # Drop each ball and record the result
        return [drop_ball(i) for i in range(n)]
