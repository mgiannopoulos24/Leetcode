from typing import List
from collections import deque

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1 and i != j:
                    adj[i].append(j)
        
        initial_sorted = sorted(initial)
        min_spread = float('inf')
        candidate = initial_sorted[0]
        
        for node in initial_sorted:
            visited = [False] * n
            visited[node] = True  # Remove the node by marking it visited
            queue = deque()
            
            for init_node in initial_sorted:
                if init_node == node or visited[init_node]:
                    continue
                queue.append(init_node)
                visited[init_node] = True
                while queue:
                    current = queue.popleft()
                    for neighbor in adj[current]:
                        if neighbor != node and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
            
            spread = sum(visited)
            if spread < min_spread:
                min_spread = spread
                candidate = node
            elif spread == min_spread and node < candidate:
                candidate = node
        
        return candidate
