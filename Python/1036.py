from typing import List, Set, Tuple
from collections import deque

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        BLOCK_LIMIT = 200
        MAX_EXPLORE = BLOCK_LIMIT * (BLOCK_LIMIT - 1) // 2  # Approximate max region that can be enclosed

        blocked_set = set(map(tuple, blocked))  # Convert to set for fast lookup
        
        def bfs(start: Tuple[int, int], goal: Tuple[int, int]) -> bool:
            queue = deque([start])
            visited = set([start])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            while queue and len(visited) <= MAX_EXPLORE:
                x, y = queue.popleft()
                if (x, y) == goal:
                    return True
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in visited and (nx, ny) not in blocked_set:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            
            return len(visited) > MAX_EXPLORE
        
        # BFS from source to target and target to source
        return bfs(tuple(source), tuple(target)) and bfs(tuple(target), tuple(source))
