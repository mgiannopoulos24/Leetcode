from collections import deque

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Check if the given position is valid for the snake's head.
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n and grid[x][y] == 0
        
        # BFS Initialization
        # Each state in the queue will be (x, y, orientation), and moves count
        # orientation is 0 for horizontal, 1 for vertical
        queue = deque([(0, 0, 0, 0)])  # (x, y, orientation, moves)
        visited = set([(0, 0, 0)])  # (x, y, orientation)

        while queue:
            x, y, orientation, moves = queue.popleft()
            
            # Check if we have reached the goal
            if orientation == 0 and x == n - 1 and y == n - 2:
                return moves
            
            # Move right
            if orientation == 0 and is_valid(x, y + 2):
                if (x, y + 1, 0) not in visited:
                    visited.add((x, y + 1, 0))
                    queue.append((x, y + 1, 0, moves + 1))
            elif orientation == 1 and is_valid(x, y + 1) and is_valid(x + 1, y + 1):
                if (x, y + 1, 1) not in visited:
                    visited.add((x, y + 1, 1))
                    queue.append((x, y + 1, 1, moves + 1))

            # Move down
            if orientation == 0 and is_valid(x + 1, y) and is_valid(x + 1, y + 1):
                if (x + 1, y, 0) not in visited:
                    visited.add((x + 1, y, 0))
                    queue.append((x + 1, y, 0, moves + 1))
            elif orientation == 1 and is_valid(x + 2, y):
                if (x + 1, y, 1) not in visited:
                    visited.add((x + 1, y, 1))
                    queue.append((x + 1, y, 1, moves + 1))

            # Rotate clockwise (from horizontal to vertical)
            if orientation == 0 and is_valid(x + 1, y) and is_valid(x + 1, y + 1):
                if (x, y, 1) not in visited:
                    visited.add((x, y, 1))
                    queue.append((x, y, 1, moves + 1))

            # Rotate counterclockwise (from vertical to horizontal)
            if orientation == 1 and is_valid(x, y + 1) and is_valid(x + 1, y + 1):
                if (x, y, 0) not in visited:
                    visited.add((x, y, 0))
                    queue.append((x, y, 0, moves + 1))

        # If we exhaust all possibilities and do not reach the goal, return -1
        return -1
