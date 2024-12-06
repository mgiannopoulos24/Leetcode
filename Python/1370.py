from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        # Step 1: Create a frequency counter of the string
        freq = Counter(s)
        
        result = []
        unique_chars = sorted(freq.keys())  # Get all unique characters sorted
        
        while len(result) < len(s):
            # Step 2: Pick characters in increasing order
            for char in unique_chars:
                if freq[char] > 0:
                    result.append(char)
                    freq[char] -= 1

            # Step 3: Pick characters in decreasing order
            for char in reversed(unique_chars):
                if freq[char] > 0:
                    result.append(char)
                    freq[char] -= 1
        
        return ''.join(result)
