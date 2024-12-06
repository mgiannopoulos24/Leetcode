from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # Helper function for checking if it's possible to reach the bottom-right
        # using only edges with effort <= max_effort
        def canReachDestination(max_effort):
            # BFS starting from (0, 0)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            queue = deque([(0, 0)])
            visited = set((0, 0))
            
            while queue:
                x, y = queue.popleft()
                
                if (x, y) == (rows - 1, cols - 1):
                    return True
                
                # Explore neighbors
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                        # Calculate the effort for moving to the neighbor
                        if abs(heights[nx][ny] - heights[x][y]) <= max_effort:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
            
            return False
        
        # Binary search for the minimum effort
        left, right = 0, max(max(row) for row in heights)  # The max possible height difference
        
        while left < right:
            mid = (left + right) // 2
            if canReachDestination(mid):
                right = mid  # Try to minimize effort
            else:
                left = mid + 1  # Increase the allowed effort
        
        return left
