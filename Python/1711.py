from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(deliciousness)
        
        # Precompute powers of two up to the largest possible sum
        powers_of_two = [1 << i for i in range(22)]
        
        freq_map = defaultdict(int)
        count = 0
        
        for val in deliciousness:
            # Check if (power of 2 - val) exists in freq_map
            for power in powers_of_two:
                target = power - val
                if target in freq_map:
                    count = (count + freq_map[target]) % MOD
            
            # Add current value to the frequency map
            freq_map[val] += 1
        
        return count
