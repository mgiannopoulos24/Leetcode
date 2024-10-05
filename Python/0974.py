from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        remainder_count = defaultdict(int)
        remainder_count[0] = 1  # To handle the case where a prefix sum itself is divisible by k
        
        for num in nums:
            prefix_sum += num
            remainder = (prefix_sum % k + k) % k  # Ensure the remainder is non-negative
            
            count += remainder_count[remainder]  # Add the number of times this remainder has been seen
            
            remainder_count[remainder] += 1  # Update the count for this remainder
        
        return count
