class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Helper function to find the root (with path compression)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Helper function to union two characters (with lexicographical order)
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                # Union by lexicographical order
                if rootX < rootY:
                    parent[rootY] = rootX
                else:
                    parent[rootX] = rootY
        
        # Initialize the parent for each character (from 'a' to 'z')
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        
        # Union the pairs from s1 and s2
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        # Build the result by finding the smallest equivalent for each character in baseStr
        result = [find(c) for c in baseStr]
        
        return ''.join(result)
