from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the greed factors and cookie sizes
        g.sort()
        s.sort()
        
        child_i = 0  # Pointer for children
        cookie_j = 0  # Pointer for cookies
        
        # Iterate through cookies and children
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                # Cookie can satisfy the child
                child_i += 1  # Move to the next child
            # Move to the next cookie
            cookie_j += 1
        
        # The number of satisfied children is the number we have moved the child pointer
        return child_i
