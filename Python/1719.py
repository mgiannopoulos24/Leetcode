class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
    # Build the adjacency set for each node
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)
        
        # Sort nodes by their degree (number of pairs they're in)
        nodes = sorted(adj.keys(), key=lambda x: len(adj[x]))
        
        # Check if any node is paired with all other nodes (potential root)
        root_candidates = [node for node in adj if len(adj[node]) == len(adj) - 1]
        if not root_candidates:
            return 0
        
        # Flag to check if multiple valid trees are possible
        multiple_ways = False
        
        # Process each node from highest degree to lowest
        for node in reversed(nodes):
            # Find a parent for the current node
            parent = None
            parent_degree = float('inf')
            
            # Find the lowest degree neighbor that can be a parent
            for neighbor in adj[node]:
                if len(adj[neighbor]) < parent_degree and len(adj[neighbor]) >= len(adj[node]):
                    parent = neighbor
                    parent_degree = len(adj[neighbor])
            
            # Skip the root node
            if parent is None:
                continue
            
            # Check if parent has all the neighbors of the current node
            for neighbor in adj[node]:
                if neighbor != parent and neighbor not in adj[parent]:
                    return 0
            
            # If parent and node have the same degree, they can swap roles
            if len(adj[parent]) == len(adj[node]):
                multiple_ways = True
        
        return 2 if multiple_ways else 1