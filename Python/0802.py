from typing import List
from collections import deque, defaultdict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        in_degree = [0] * n
        
        # Step 1: Reverse the graph and compute in-degrees
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
                in_degree[u] += 1
        
        # Step 2: Collect nodes with in-degree of 0 (terminal nodes)
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Step 3: Process the queue using BFS
        safe_nodes = []
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Sort the safe nodes and return them
        return sorted(safe_nodes)