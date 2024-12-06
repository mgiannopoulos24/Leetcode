from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # If k is large enough to eliminate all obstacles on the path, return (m + n - 2)
        if k >= m + n - 2:
            return m + n - 2

        # Initialize visited matrix with -1
        # visited[x][y] = minimum obstacles eliminated to reach (x, y)
        visited = [[-1 for _ in range(n)] for _ in range(m)]
        visited[0][0] = 0

        # BFS Queue: (x, y, obstacles_eliminated)
        queue = deque()
        queue.append((0, 0, 0))

        steps = 0  # Number of steps taken

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            for _ in range(len(queue)):
                x, y, eliminated = queue.popleft()

                # If reached the destination, return steps
                if x == m - 1 and y == n - 1:
                    return steps

                # Explore all possible directions
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # Check boundaries
                    if 0 <= nx < m and 0 <= ny < n:
                        new_eliminated = eliminated + grid[nx][ny]

                        # If new_eliminated exceeds k, skip
                        if new_eliminated > k:
                            continue

                        # If this path to (nx, ny) has fewer obstacles eliminated, proceed
                        if visited[nx][ny] == -1 or new_eliminated < visited[nx][ny]:
                            visited[nx][ny] = new_eliminated
                            queue.append((nx, ny, new_eliminated))

            steps += 1  # Increment steps after exploring all nodes at current level

        # Destination not reachable
        return -1
