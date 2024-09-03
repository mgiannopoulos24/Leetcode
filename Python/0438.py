from collections import defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return []
        
        # Frequency counters
        p_count = [0] * 26
        s_count = [0] * 26
        
        # Fill frequency counter for p
        for char in p:
            p_count[ord(char) - ord('a')] += 1
        
        # Initial window in s
        for i in range(len_p):
            s_count[ord(s[i]) - ord('a')] += 1
        
        result = []
        
        # Check if the first window is an anagram
        if s_count == p_count:
            result.append(0)
        
        # Sliding the window across s
        for i in range(len_p, len_s):
            # Add new character to the window
            s_count[ord(s[i]) - ord('a')] += 1
            # Remove the character that is sliding out of the window
            s_count[ord(s[i - len_p]) - ord('a')] -= 1
            
            # Compare current window with p
            if s_count == p_count:
                result.append(i - len_p + 1)
        
        return result
