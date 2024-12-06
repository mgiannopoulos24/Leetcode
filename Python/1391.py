from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # Grid dimensions
        m, n = len(grid), len(grid[0])
        
        # Map for each street type with possible directions
        directions = {
            1: [(0, -1), (0, 1)],   # Left and Right
            2: [(-1, 0), (1, 0)],   # Up and Down
            3: [(0, -1), (1, 0)],   # Left and Down
            4: [(0, 1), (1, 0)],    # Right and Down
            5: [(0, -1), (-1, 0)],  # Left and Up
            6: [(0, 1), (-1, 0)]    # Right and Up
        }
        
        # Valid street pairings that allow movement between neighboring cells
        valid_connection = {
            (1, (0, -1)): [1, 4, 6], (1, (0, 1)): [1, 3, 5],
            (2, (-1, 0)): [2, 3, 4], (2, (1, 0)): [2, 5, 6],
            (3, (0, -1)): [1, 4, 6], (3, (1, 0)): [2, 5, 6],
            (4, (0, 1)): [1, 3, 5], (4, (1, 0)): [2, 5, 6],
            (5, (0, -1)): [1, 4, 6], (5, (-1, 0)): [2, 3, 4],
            (6, (0, 1)): [1, 3, 5], (6, (-1, 0)): [2, 3, 4]
        }
        
        # BFS setup
        queue = deque([(0, 0)])  # Start from the top-left corner
        visited = set()
        visited.add((0, 0))
        
        while queue:
            x, y = queue.popleft()
            
            # If we reach the bottom-right corner, return True
            if (x, y) == (m - 1, n - 1):
                return True
            
            # Explore all possible directions based on the current cell's street type
            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                # Ensure that the next position is within bounds and not visited yet
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    # Check if the next street can connect back to the current cell
                    if grid[nx][ny] in valid_connection[(grid[x][y], (dx, dy))]:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        # If we exhaust all possibilities and do not reach the bottom-right corner
        return False
