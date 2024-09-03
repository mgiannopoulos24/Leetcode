from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        
        m, n = len(mat), len(mat[0])
        # Initialize distance matrix with infinity for 1s and 0s for 0s
        dist = [[float('inf')] * n for _ in range(m)]
        queue = deque()
        
        # Enqueue all 0 cells and set their distance to 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        
        # Directions for moving in the matrix (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # BFS to compute shortest distance
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # If we found a shorter distance to (nx, ny)
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
        
        return dist
