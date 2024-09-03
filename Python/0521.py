class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # Check if strings are identical
        if a == b:
            return -1
        
        # Return the length of the longer string
        return max(len(a), len(b))
