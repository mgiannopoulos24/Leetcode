class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        n = len(s)
        
        i = 0
        while i < n:
            start = i
            # Move 'i' forward to find the end of the current group
            while i < n and s[i] == s[start]:
                i += 1
            # Now, 'i' is at the position after the last occurrence of s[start]
            if i - start >= 3:
                result.append([start, i - 1])
        
        return result
