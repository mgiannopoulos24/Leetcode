from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Convert board to string format for easier comparison and manipulation
        start = ''.join(map(str, board[0] + board[1]))
        target = "123450"
        
        # Early return if the start is already the target
        if start == target:
            return 0
        
        # Directions for moving the zero: (row, col) -> (row, col) transformations
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pos = {0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (1, 0), 4: (1, 1), 5: (1, 2)}
        
        # BFS setup
        queue = deque([(start, start.index('0'), 0)])
        visited = set([start])
        
        while queue:
            state, zero_idx, moves = queue.popleft()
            zero_row, zero_col = pos[zero_idx]
            
            # Try all possible directions
            for dr, dc in directions:
                new_row, new_col = zero_row + dr, zero_col + dc
                if 0 <= new_row < 2 and 0 <= new_col < 3:
                    new_zero_idx = new_row * 3 + new_col
                    new_state_list = list(state)
                    # Swap zero with the adjacent number
                    new_state_list[zero_idx], new_state_list[new_zero_idx] = new_state_list[new_zero_idx], new_state_list[zero_idx]
                    new_state = ''.join(new_state_list)
                    
                    if new_state == target:
                        return moves + 1
                    
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, new_zero_idx, moves + 1))
        
        return -1
