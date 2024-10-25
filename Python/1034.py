from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        original_color = grid[row][col]
        visited = [[False] * n for _ in range(m)]
        borders = []

        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_border(r, c):
            # A cell is a border if it's on the boundary or has a neighbor with a different color
            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] != original_color:
                    return True
            return False

        def dfs(r, c):
            visited[r][c] = True
            if is_border(r, c):
                borders.append((r, c))

            # Explore all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == original_color:
                    dfs(nr, nc)

        # Start DFS from the initial position (row, col)
        dfs(row, col)

        # Color all the borders found
        for r, c in borders:
            grid[r][c] = color

        return grid
