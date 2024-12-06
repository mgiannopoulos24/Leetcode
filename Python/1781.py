from collections import defaultdict

class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)
        
        # Iterate over each possible starting point for substrings
        for i in range(n):
            # Initialize frequency map for the current starting position
            freq = [0] * 26
            
            # Expand the substring from current starting point `i` to the end of the string
            for j in range(i, n):
                # Update the frequency map for the current character
                freq[ord(s[j]) - ord('a')] += 1
                
                # Get non-zero frequencies for calculation
                non_zero_freq = [f for f in freq if f > 0]
                
                # Calculate beauty: max frequency - min frequency
                if non_zero_freq:
                    max_freq = max(non_zero_freq)
                    min_freq = min(non_zero_freq)
                    total_beauty += max_freq - min_freq

        return total_beauty
