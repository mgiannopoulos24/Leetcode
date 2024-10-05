from typing import List, Set, Dict
from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(node, visited, graph):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
        
        graph = defaultdict(list)
        for x, y in stones:
            graph[('row', x)].append(('col', y))
            graph[('col', y)].append(('row', x))
        
        visited = set()
        components = 0
        
        for x, y in stones:
            if ('row', x) not in visited:
                components += 1
                visited.add(('row', x))
                dfs(('row', x), visited, graph)
        
        return len(stones) - components
