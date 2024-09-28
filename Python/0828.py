from collections import defaultdict
from typing import List

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        Calculate the sum of unique characters of all substrings of s.
        
        :param s: Input string consisting of uppercase English letters.
        :return: The total sum of unique characters across all substrings of s.
        """
        # Dictionary to store all indices for each character
        char_indices = defaultdict(list)
        
        # Populate the dictionary with character indices
        for i, c in enumerate(s):
            char_indices[c].append(i)
        
        total = 0
        n = len(s)
        MOD = 10**9 + 7  # To handle large numbers, if required
        
        # Iterate through each character and its list of indices
        for c, indices in char_indices.items():
            # Pad the indices with -1 at the beginning and n at the end
            # This helps in handling edge cases where there is no previous or next occurrence
            padded_indices = [-1] + indices + [n]
            
            # Iterate through each occurrence of the character
            for i in range(1, len(padded_indices) - 1):
                # Current index of the character
                current = padded_indices[i]
                # Previous index of the character
                prev = padded_indices[i - 1]
                # Next index of the character
                nex = padded_indices[i + 1]
                
                # The number of substrings where s[current] is unique:
                # (current - prev) * (nex - current)
                left = current - prev
                right = nex - current
                contribution = left * right
                
                # Add the contribution to the total
                total += contribution
                # If needed, use modulo to keep the number within bounds
                # total %= MOD
        
        return total % MOD  # Return the result modulo 10^9 + 7

