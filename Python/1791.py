from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Check the first two edges and find the common node
        u1, v1 = edges[0]
        u2, v2 = edges[1]
        
        # The center node is the one that appears in both edges
        if u1 == u2 or u1 == v2:
            return u1
        return v1
