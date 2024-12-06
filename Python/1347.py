from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Step 1: Count frequencies of each character in s and t
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Step 2: Calculate how many changes are needed
        steps = 0
        
        # Step 3: Iterate over the counts in s and t, and count the excess characters in t
        for char in count_s:
            if count_s[char] > count_t[char]:
                steps += count_s[char] - count_t[char]
        
        return steps
