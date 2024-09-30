from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        
        r, c = rStart, cStart
        steps = 1
        dir_idx = 0
        
        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    if in_bounds(r, c):
                        result.append([r, c])
                    dr, dc = directions[dir_idx]
                    r += dr
                    c += dc
                dir_idx = (dir_idx + 1) % 4
            steps += 1
        
        return result