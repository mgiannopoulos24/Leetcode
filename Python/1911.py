from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even, odd = 0, 0  # Initialize states
        
        for num in nums:
            # Update states
            new_even = max(even, odd + num)
            new_odd = max(odd, even - num)
            even, odd = new_even, new_odd
        
        return even  # Maximum alternating sum is in the "even" state
