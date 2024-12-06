class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Step 1: Build the tree as an adjacency list
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Perform DFS and calculate the minimum time
        def dfs(node, parent):
            total_time = 0
            # Visit all the children
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                time_from_subtree = dfs(neighbor, node)
                # If the subtree rooted at 'neighbor' has apples, we need to add the time
                if time_from_subtree > 0 or hasApple[neighbor]:
                    total_time += time_from_subtree + 2
            
            return total_time
        
        # Start DFS from the root (node 0)
        return dfs(0, -1)

