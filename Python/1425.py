from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        deq = deque([0])  # Stores indices of dp in decreasing order
        max_sum = nums[0]
        
        for i in range(1, n):
            # Remove indices from deque that are out of range (more than k distance)
            if deq[0] < i - k:
                deq.popleft()
            
            # dp[i] is the current element + max of dp within the last k elements
            dp[i] = nums[i] + max(0, dp[deq[0]])
            max_sum = max(max_sum, dp[i])
            
            # Maintain the deque in a way that dp[deq] is decreasing
            while deq and dp[deq[-1]] <= dp[i]:
                deq.pop()
            
            deq.append(i)
        
        return max_sum
