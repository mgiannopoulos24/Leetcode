from typing import List, Tuple
from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        """
        Returns the minimum number of pushes to move the box 'B' to the target 'T'.
        If it's impossible, returns -1.
        """
        m, n = len(grid), len(grid[0])
        # Directions: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Locate positions of S, B, T
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    player_start = (i, j)
                elif grid[i][j] == 'B':
                    box_start = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)

        # Helper function to check if a position is within the grid and not a wall
        def is_valid(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n and grid[x][y] != '#'

        # Helper function to perform BFS to check if the player can reach (tx, ty) from (sx, sy)
        # without crossing the box position (bx, by)
        def can_reach(sx: int, sy: int, tx: int, ty: int, bx: int, by: int) -> bool:
            visited = [[False for _ in range(n)] for _ in range(m)]
            queue = deque()
            queue.append((sx, sy))
            visited[sx][sy] = True
            while queue:
                x, y = queue.popleft()
                if x == tx and y == ty:
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny) and not visited[nx][ny] and (nx, ny) != (bx, by):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return False

        # BFS Queue: each element is (pushes, box_x, box_y, player_x, player_y)
        queue = deque()
        queue.append((0, box_start[0], box_start[1], player_start[0], player_start[1]))
        # Visited set: (box_x, box_y, player_x, player_y)
        visited = set()
        visited.add((box_start[0], box_start[1], player_start[0], player_start[1]))

        while queue:
            pushes, bx, by, px, py = queue.popleft()
            # Check if box is at target
            if (bx, by) == target:
                return pushes
            # Try all four directions to push the box
            for dx, dy in dirs:
                new_bx, new_by = bx + dx, by + dy  # New box position after push
                # The position where the player needs to be to push the box
                required_px, required_py = bx - dx, by - dy
                # Check if new box position is valid
                if not is_valid(new_bx, new_by):
                    continue
                # Check if required player position is valid
                if not is_valid(required_px, required_py):
                    continue
                # Check if the player can reach the required position without crossing the box
                if not can_reach(px, py, required_px, required_py, bx, by):
                    continue
                # After pushing, the player will be at the box's current position
                new_px, new_py = bx, by
                # Check if this state has been visited
                if (new_bx, new_by, new_px, new_py) in visited:
                    continue
                visited.add((new_bx, new_by, new_px, new_py))
                queue.append((pushes + 1, new_bx, new_by, new_px, new_py))
        # If target is not reachable
        return -1
