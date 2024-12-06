from typing import List
from collections import defaultdict

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list and degree count for each node
        graph = defaultdict(set)
        degrees = [0] * (n + 1)  # degree of each node (1-based index)
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degrees[u] += 1
            degrees[v] += 1
        
        # Step 2: Find all connected trios and calculate their degrees
        min_degree = float('inf')
        
        for u in range(1, n + 1):
            for v in graph[u]:
                if v > u:  # only consider pairs (u, v) once
                    for w in graph[u]:
                        if w > v and w in graph[v]:  # Check if w is connected to both u and v
                            # Calculate the trio degree
                            current_degree = degrees[u] + degrees[v] + degrees[w] - 6
                            min_degree = min(min_degree, current_degree)
        
        # Step 3: If min_degree was updated, return it, otherwise return -1
        return min_degree if min_degree != float('inf') else -1
