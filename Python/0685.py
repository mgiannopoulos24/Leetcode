class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))  # To keep track of each node's parent
        candidate1 = candidate2 = None  # Possible edges causing two parents
        
        # Step 1: Check for a node with two parents
        root_parent = {}
        for u, v in edges:
            if v in root_parent:
                candidate1 = [root_parent[v], v]  # First parent
                candidate2 = [u, v]  # Second parent
                continue
            root_parent[v] = u
        
        # Union-Find to detect cycles
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Union-Find to check for cycles
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True
        
        # Step 2: Try removing candidate2 first, if any, and check if a cycle exists
        parent = list(range(n + 1))  # Reset parent array
        for u, v in edges:
            if [u, v] == candidate2:  # Skip candidate2 if it exists
                continue
            if not union(u, v):
                # Cycle detected
                if candidate1:
                    return candidate1
                return [u, v]
        
        # If there's no cycle, return candidate2
        return candidate2
