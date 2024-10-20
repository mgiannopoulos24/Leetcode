from collections import Counter
from typing import List

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Directions for turning off the lamp and its 8 adjacent cells
        directions = [(0, 0), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
        
        # Counters to track number of lamps affecting rows, cols, diagonals, and anti-diagonals
        row = Counter()
        col = Counter()
        diag = Counter()
        anti_diag = Counter()
        lamps_set = set()  # Track active lamps as a set
        
        # Initialize the counters based on the initial set of lamps
        for r, c in lamps:
            if (r, c) not in lamps_set:
                lamps_set.add((r, c))
                row[r] += 1
                col[c] += 1
                diag[r - c] += 1
                anti_diag[r + c] += 1
        
        result = []
        
        # Process each query
        for qr, qc in queries:
            # Check if the cell is illuminated
            if row[qr] > 0 or col[qc] > 0 or diag[qr - qc] > 0 or anti_diag[qr + qc] > 0:
                result.append(1)
            else:
                result.append(0)
            
            # Turn off the lamp at (qr, qc) and its 8 adjacent cells
            for dr, dc in directions:
                nr, nc = qr + dr, qc + dc
                if (nr, nc) in lamps_set:
                    lamps_set.remove((nr, nc))
                    row[nr] -= 1
                    col[nc] -= 1
                    diag[nr - nc] -= 1
                    anti_diag[nr + nc] -= 1
        
        return result
