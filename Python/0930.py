from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Base case: for the subarrays that start from index 0
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num
            # Check how many times (current_sum - goal) has occurred
            if (current_sum - goal) in prefix_sum_count:
                result += prefix_sum_count[current_sum - goal]
            # Update the hash map with the current prefix_sum
            prefix_sum_count[current_sum] += 1
        
        return result
