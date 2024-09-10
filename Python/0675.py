from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(start, end):
            """ Perform BFS to find the shortest path from start to end """
            if start == end:
                return 0
            
            rows, cols = len(forest), len(forest[0])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            queue = deque([start])
            visited = set()
            visited.add(start)
            steps = 0
            
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if (r, c) == end:
                        return steps
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and
                                (nr, nc) not in visited and forest[nr][nc] > 0):
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                steps += 1
            
            return -1
        
        # Step 1: Collect all trees and sort them by height
        trees = []
        for r in range(len(forest)):
            for c in range(len(forest[0])):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
        
        trees.sort()  # Sort trees by height
        
        # Step 2: Traverse from (0, 0) to each tree in sorted order
        current_pos = (0, 0)
        total_steps = 0
        
        for _, tr, tc in trees:
            steps = bfs(current_pos, (tr, tc))
            if steps == -1:
                return -1
            total_steps += steps
            current_pos = (tr, tc)
        
        return total_steps
