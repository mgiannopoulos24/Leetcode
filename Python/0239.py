from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # List to store the result
        result = []
        # Deque to store indices of the current window's elements
        deq = deque()
        
        for i, num in enumerate(nums):
            # Remove indices from the front of the deque that are out of the current window
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # Remove indices from the back of the deque while the value at those indices is less than the current number
            while deq and nums[deq[-1]] < num:
                deq.pop()
            
            # Add the current index to the deque
            deq.append(i)
            
            # The current window's maximum value is at the front of the deque
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result
