from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Array to store counts of remainders
        remainders = [0] * 60
        count = 0
        
        for t in time:
            # Calculate remainder
            remainder = t % 60
            # Find the complement remainder that would sum to 60
            complement = (60 - remainder) % 60
            # Add the number of valid pairs
            count += remainders[complement]
            # Increment the count for this remainder
            remainders[remainder] += 1
        
        return count
