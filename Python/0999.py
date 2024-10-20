from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find the position of the rook
        rook_row, rook_col = -1, -1
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    rook_row, rook_col = r, c
                    break
            if rook_row != -1:
                break
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        
        # Traverse in each direction
        for dr, dc in directions:
            r, c = rook_row, rook_col
            while 0 <= r < 8 and 0 <= c < 8:
                r += dr
                c += dc
                if 0 <= r < 8 and 0 <= c < 8:
                    if board[r][c] == 'B':
                        break  # Blocked by bishop
                    elif board[r][c] == 'p':
                        count += 1
                        break  # Pawn found, stop in this direction
                else:
                    break  # Out of bounds
        
        return count
