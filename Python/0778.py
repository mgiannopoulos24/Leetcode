from typing import List
from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4-directional movements

        def canReach(t: int) -> bool:
            if grid[0][0] > t:
                return False
            visited = set()
            queue = deque([(0, 0)])
            visited.add((0, 0))
            
            while queue:
                x, y = queue.popleft()
                if (x, y) == (n - 1, n - 1):
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] <= t:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return False
        
        # Binary search on the time
        left, right = 0, max(max(row) for row in grid)
        while left < right:
            mid = (left + right) // 2
            if canReach(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
