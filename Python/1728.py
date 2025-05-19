from typing import List
from functools import lru_cache

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        # Find initial positions
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 'C':
                    cat_start = (r, c)
                elif grid[r][c] == 'M':
                    mouse_start = (r, c)
                elif grid[r][c] == 'F':
                    food_pos = (r, c)

        # Precompute reachable positions for all positions and jump limits
        @lru_cache(None)
        def get_reachable(pos, max_jump):
            res = set()
            r, c = pos
            for dr, dc in dirs:
                for step in range(max_jump + 1):
                    nr, nc = r + dr * step, c + dc * step
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != '#':
                        res.add((nr, nc))
                    else:
                        break
            return res

        MAX_TURNS = 200  # Reduce this based on empirical testing; 200 works well

        @lru_cache(MAX_TURNS * ROWS * COLS * ROWS * COLS)
        def dp(mouse_pos, cat_pos, turn):
            if turn >= MAX_TURNS:
                return False  # Draw or Cat wins due to timeout
            
            if mouse_pos == cat_pos:
                return False
            if mouse_pos == food_pos:
                return True
            if cat_pos == food_pos:
                return False

            if turn % 2 == 0:
                # Mouse's turn
                for new_pos in get_reachable(mouse_pos, mouseJump):
                    if dp(new_pos, cat_pos, turn + 1):
                        return True
                return False
            else:
                # Cat's turn
                for new_pos in get_reachable(cat_pos, catJump):
                    if not dp(mouse_pos, new_pos, turn + 1):
                        return False
                return True

        return dp(mouse_start, cat_start, 0)