from collections import deque
from typing import List, Tuple

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def bfs(start_nodes: List[Tuple[int, int]]) -> int:
            queue = deque(start_nodes)
            distances = {}
            for (x, y) in start_nodes:
                distances[(x, y)] = 0
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in distances:
                        if grid[nx][ny] == 3:
                            return distances[(x, y)]  # Reached the second island
                        distances[(nx, ny)] = distances[(x, y)] + 1
                        queue.append((nx, ny))
            return -1  # This should never happen given the problem constraints

        def dfs(x: int, y: int, mark: int) -> List[Tuple[int, int]]:
            stack = [(x, y)]
            cells = []
            while stack:
                cx, cy = stack.pop()
                if (cx, cy) in visited or not (0 <= cx < n and 0 <= cy < n) or grid[cx][cy] != 1:
                    continue
                visited.add((cx, cy))
                grid[cx][cy] = mark
                cells.append((cx, cy))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    stack.append((cx + dx, cy + dy))
            return cells
        
        n = len(grid)
        visited = set()
        
        # Find and mark the first island with 2
        first_island_cells = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    first_island_cells = dfs(i, j, 2)
                    break
            if first_island_cells:
                break
        
        # Find and mark the second island with 3
        second_island_cells = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    second_island_cells = dfs(i, j, 3)
                    break
            if second_island_cells:
                break
        
        # Perform BFS from the first island to find the shortest path to the second island
        return bfs(first_island_cells)
