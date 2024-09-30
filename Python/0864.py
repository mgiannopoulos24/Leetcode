from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        # Find start position and number of keys
        start = None
        num_keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif 'a' <= grid[i][j] <= 'f':
                    num_keys = max(num_keys, ord(grid[i][j]) - ord('a') + 1)
        
        # Directions for moving in the grid
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS setup
        queue = deque([(start[0], start[1], 0, 0)])  # (x, y, steps, keys_bitmask)
        visited = set()
        visited.add((start[0], start[1], 0))
        
        while queue:
            x, y, steps, keys = queue.popleft()
            
            # Check if all keys are collected
            if keys == (1 << num_keys) - 1:
                return steps
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]
                    
                    # If the cell is a wall, skip
                    if cell == '#':
                        continue
                    
                    # If the cell is a key, update the keys bitmask
                    if 'a' <= cell <= 'f':
                        new_keys = keys | (1 << (ord(cell) - ord('a')))
                    else:
                        new_keys = keys
                    
                    # If the cell is a lock, check if we have the key
                    if 'A' <= cell <= 'F':
                        if not (keys & (1 << (ord(cell) - ord('A')))):
                            continue
                    
                    # If not visited, add to the queue
                    if (nx, ny, new_keys) not in visited:
                        visited.add((nx, ny, new_keys))
                        queue.append((nx, ny, steps + 1, new_keys))
        
        # If all keys cannot be collected
        return -1
