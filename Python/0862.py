from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        # Compute the prefix sums
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Initialize deque and result
        min_length = float('inf')
        dq = deque()
        
        for i in range(n + 1):
            # Check if the current prefix sum minus the smallest prefix sum in deque is at least k
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            
            # Maintain the deque with indices of prefix sums
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return min_length if min_length != float('inf') else -1
