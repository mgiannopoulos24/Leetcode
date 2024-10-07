from collections import defaultdict
from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        # Initialize dictionary to count pairwise AND results
        pairwise_and_count = defaultdict(int)
        
        # Count how many times each AND result occurs for all pairs (i, j)
        for i in range(len(nums)):
            for j in range(len(nums)):
                pairwise_and_count[nums[i] & nums[j]] += 1
        
        # Initialize the result for counting valid triples
        result = 0
        
        # Check for each number in the array
        for num in nums:
            for key in pairwise_and_count:
                if key & num == 0:
                    result += pairwise_and_count[key]
        
        return result
