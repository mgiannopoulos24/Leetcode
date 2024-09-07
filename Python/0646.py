from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs by their second element
        pairs.sort(key=lambda x: x[1])
        
        # Initialize variables
        longest_chain_length = 0
        last_end = float('-inf')
        
        # Iterate through sorted pairs
        for pair in pairs:
            if pair[0] > last_end:
                # Can include this pair in the chain
                longest_chain_length += 1
                last_end = pair[1]
        
        return longest_chain_length
