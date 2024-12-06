from typing import List

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # Initialize the grid as a 2D list filled with False (uncovered)
        grid = [[False] * m for _ in range(n)]
        self.min_squares = float('inf')
        
        def find_next():
            # Find the top-leftmost uncovered cell
            for i in range(n):
                for j in range(m):
                    if not grid[i][j]:
                        return i, j
            return -1, -1  # All cells are covered
        
        def backtrack(count):
            # If count already exceeds or equals the current minimum, prune
            if count >= self.min_squares:
                return
            
            # Find the next cell to cover
            x, y = find_next()
            if x == -1:
                # All cells are covered
                self.min_squares = min(self.min_squares, count)
                return
            
            # Determine the maximum size of the square that can be placed at (x, y)
            max_size = min(n - x, m - y)
            # Further limit the max_size based on already placed squares
            for size in range(max_size, 0, -1):
                # Check if the square of this size can be placed
                can_place = True
                for i in range(x, x + size):
                    for j in range(y, y + size):
                        if grid[i][j]:
                            can_place = False
                            break
                    if not can_place:
                        break
                if can_place:
                    # Place the square
                    for i in range(x, x + size):
                        for j in range(y, y + size):
                            grid[i][j] = True
                    # Recurse
                    backtrack(count + 1)
                    # Remove the square (backtrack)
                    for i in range(x, x + size):
                        for j in range(y, y + size):
                            grid[i][j] = False
        
        backtrack(0)
        return self.min_squares
