from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character
        count = Counter(s)
        
        # Sort characters by frequency (highest first) and then by character if needed
        sorted_chars = sorted(count.keys(), key=lambda x: (-count[x], x))
        
        # Build the result string based on sorted characters and their frequencies
        result = ''.join(char * count[char] for char in sorted_chars)
        
        return result
