from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bitmasks = [0] * n
        lengths = [0] * n
        
        # Step 1: Calculate bitmasks and lengths
        for i in range(n):
            bitmask = 0
            for char in words[i]:
                bitmask |= (1 << (ord(char) - ord('a')))
            bitmasks[i] = bitmask
            lengths[i] = len(words[i])
        
        max_product = 0
        
        # Step 2: Find the maximum product of lengths of two words with no common characters
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0:  # No common letters
                    max_product = max(max_product, lengths[i] * lengths[j])
        
        return max_product