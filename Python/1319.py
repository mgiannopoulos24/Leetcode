class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # If we don't have enough cables to connect all computers
        if len(connections) < n - 1:
            return -1
        
        # Build the graph (adjacency list)
        graph = {i: [] for i in range(n)}
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # To count the number of connected components
        def dfs(node, visited):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
        
        visited = set()
        components = 0
        
        # Perform DFS to count components
        for i in range(n):
            if i not in visited:
                components += 1
                visited.add(i)
                dfs(i, visited)
        
        # We need (components - 1) cables to connect all components
        return components - 1
