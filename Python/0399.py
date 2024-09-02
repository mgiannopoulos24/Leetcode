from typing import List, Dict, Tuple

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the graph
        graph = {}
        
        def add_edge(start: str, end: str, value: float) -> None:
            if start not in graph:
                graph[start] = []
            if end not in graph:
                graph[end] = []
            graph[start].append((end, value))
            graph[end].append((start, 1 / value))
        
        # Add all edges to the graph
        for (u, v), value in zip(equations, values):
            add_edge(u, v, value)
        
        # Helper function to perform DFS
        def dfs(start: str, end: str, visited: set) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            stack = [(start, 1.0)]
            while stack:
                current, product = stack.pop()
                if current in visited:
                    continue
                visited.add(current)
                for neighbor, weight in graph[current]:
                    if neighbor == end:
                        return product * weight
                    stack.append((neighbor, product * weight))
            return -1.0
        
        # Process each query
        results = []
        for u, v in queries:
            results.append(dfs(u, v, set()))
        
        return results
