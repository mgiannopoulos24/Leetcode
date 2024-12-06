from typing import List
from collections import Counter

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # Frequency count for each character in a and b
        count_a = [0] * 26
        count_b = [0] * 26
        for char in a:
            count_a[ord(char) - ord('a')] += 1
        for char in b:
            count_b[ord(char) - ord('a')] += 1
        
        # Calculate the length of a and b
        len_a = len(a)
        len_b = len(b)
        
        # Condition 3: Make both a and b have only one distinct letter
        max_freq_a = max(count_a)
        max_freq_b = max(count_b)
        condition3_operations = (len_a - max_freq_a) + (len_b - max_freq_b)
        
        # Condition 1 and Condition 2: Cumulative sums for less-than conditions
        min_operations = condition3_operations
        cumulative_a = cumulative_b = 0
        
        for i in range(25):  # Only go up to 'y' for cutoff
            cumulative_a += count_a[i]
            cumulative_b += count_b[i]
            
            # Condition 1: All chars in `a` < all chars in `b`
            condition1_operations = (len_a - cumulative_a) + cumulative_b
            min_operations = min(min_operations, condition1_operations)
            
            # Condition 2: All chars in `b` < all chars in `a`
            condition2_operations = (len_b - cumulative_b) + cumulative_a
            min_operations = min(min_operations, condition2_operations)
        
        return min_operations
