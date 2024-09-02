from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Count frequencies of characters in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Find the character that has a different frequency in t
        for char in count_t:
            if count_t[char] > count_s.get(char, 0):
                return char
