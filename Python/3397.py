from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the input array
        used = set()  # Set to track distinct elements
        smallest_unused = -float('inf')  # Initialize the smallest unused number
        
        for num in nums:
            # Start from max(num-k, smallest_unused + 1) to ensure distinctness
            candidate = max(num - k, smallest_unused + 1)
            
            # Check if the candidate is within the valid range
            if candidate <= num + k:
                used.add(candidate)
                smallest_unused = candidate  # Update the smallest_unused pointer
        
        return len(used)  # The size of the set represents distinct elements
