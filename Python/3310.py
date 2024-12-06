from collections import defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the graph
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        for a, b in invocations:
            graph[a].append(b)
            reverse_graph[b].append(a)
        
        # Step 2: DFS from k to mark all suspicious methods
        suspicious = [False] * n
        
        def dfs(node):
            suspicious[node] = True
            for neighbor in graph[node]:
                if not suspicious[neighbor]:
                    dfs(neighbor)
        
        dfs(k)
        
        # Step 3: Check for external invocations to suspicious methods
        for i in range(n):
            if not suspicious[i]:  # For each non-suspicious method
                for neighbor in graph[i]:
                    if suspicious[neighbor]:  # If a non-suspicious method invokes a suspicious one
                        return list(range(n))  # It's not possible to remove the suspicious methods
        
        # Step 4: Return the remaining methods (non-suspicious ones)
        return [i for i in range(n) if not suspicious[i]]
