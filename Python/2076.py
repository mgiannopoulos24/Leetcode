class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        # Union-Find data structure
        parent = list(range(n))
        
        def find(x):
            # Find the root of the set containing x with path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            # Union the sets containing x and y
            parent[find(x)] = find(y)
        
        def is_connected(x, y):
            # Check if x and y are in the same connected component
            return find(x) == find(y)
        
        def will_violate_restrictions(u, v):
            # Check if connecting u and v will violate any restrictions
            root_u = find(u)
            root_v = find(v)
            
            if root_u == root_v:  # Already connected
                return False
            
            # Check each restriction
            for x, y in restrictions:
                root_x = find(x)
                root_y = find(y)
                
                # If connecting u and v would connect a restricted pair
                if (root_x == root_u and root_y == root_v) or (root_x == root_v and root_y == root_u):
                    return True
            
            return False
        
        result = []
        
        for u, v in requests:
            # Check if this request would violate restrictions
            if will_violate_restrictions(u, v):
                result.append(False)
            else:
                # Union the sets if the request is valid
                union(u, v)
                result.append(True)
        
        return result