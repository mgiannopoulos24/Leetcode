from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Check if the starting or ending cell is blocked
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        # Initialize the queue for BFS with the starting point (0, 0)
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # Mark as visited
        
        while queue:
            row, col, path_length = queue.popleft()
            
            # If we have reached the bottom-right corner, return the path length
            if row == n - 1 and col == n - 1:
                return path_length
            
            # Explore all 8 possible directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is within bounds and is an open cell
                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                    queue.append((new_row, new_col, path_length + 1))
                    grid[new_row][new_col] = 1  # Mark the cell as visited
        
        # If no path was found, return -1
        return -1
