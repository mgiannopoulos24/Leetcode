from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_neighbors(state):
            neighbors = []
            for i in range(4):
                for d in [-1, 1]:
                    new_digit = (int(state[i]) + d) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    neighbors.append(new_state)
            return neighbors

        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1

        queue = deque(["0000"])
        visited = set(["0000"])
        moves = 0

        while queue:
            for _ in range(len(queue)):
                current_state = queue.popleft()
                if current_state == target:
                    return moves
                
                for neighbor in get_neighbors(current_state):
                    if neighbor not in visited and neighbor not in deadends_set:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            moves += 1
        
        return -1
