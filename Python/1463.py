class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {}

        def dp(i, j1, j2):
            # If out of bounds, return a very small value (invalid state)
            if j1 < 0 or j1 >= cols or j2 < 0 or j2 >= cols:
                return float('-inf')
            
            # If we've reached the last row, return the cherries from both robots
            if i == rows - 1:
                if j1 == j2:
                    return grid[i][j1]  # both robots on the same cell
                else:
                    return grid[i][j1] + grid[i][j2]
            
            # Check memoization
            if (i, j1, j2) in memo:
                return memo[(i, j1, j2)]
            
            # Current cherries collected by the two robots
            result = 0
            if j1 == j2:
                result += grid[i][j1]  # both robots on the same cell
            else:
                result += grid[i][j1] + grid[i][j2]  # different cells
            
            # Try all the possible moves for both robots in the next row
            max_cherries = float('-inf')
            for new_j1 in [j1 - 1, j1, j1 + 1]:
                for new_j2 in [j2 - 1, j2, j2 + 1]:
                    max_cherries = max(max_cherries, dp(i + 1, new_j1, new_j2))
            
            result += max_cherries
            memo[(i, j1, j2)] = result
            return result
        
        # Start the dp from the top row, with Robot 1 at (0, 0) and Robot 2 at (0, cols-1)
        return dp(0, 0, cols - 1)
