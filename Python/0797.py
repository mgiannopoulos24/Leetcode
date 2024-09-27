class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node: int, path: List[int]):
            # Add current node to the path
            path.append(node)
            
            # If we reached the target node, add the path to the result
            if node == len(graph) - 1:
                result.append(path.copy())
            else:
                # Continue DFS to all connected nodes
                for neighbor in graph[node]:
                    dfs(neighbor, path)
            
            # Backtrack to explore new paths
            path.pop()
        
        result = []
        dfs(0, [])
        return result
