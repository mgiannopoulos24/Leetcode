from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are different
        if len(s) != len(t):
            return False
        
        # Count frequencies of characters in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Compare the two frequency counts
        return count_s == count_t
