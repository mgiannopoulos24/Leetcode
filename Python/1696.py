from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Initialize dp array with the first element
        dp = [0] * n
        dp[0] = nums[0]
        
        # Monotonic deque to store the indices of the maximum dp values
        deque_indices = deque([0])
        
        # Iterate through the array from 1 to n-1
        for i in range(1, n):
            # Remove indices from the deque that are out of the range of k
            if deque_indices[0] < i - k:
                deque_indices.popleft()
            
            # The current dp[i] is the maximum value in the deque + nums[i]
            dp[i] = dp[deque_indices[0]] + nums[i]
            
            # Maintain the deque: remove elements smaller than the current dp[i]
            while deque_indices and dp[deque_indices[-1]] <= dp[i]:
                deque_indices.pop()
            
            # Add the current index to the deque
            deque_indices.append(i)
        
        # The result is the maximum score at the last index
        return dp[-1]
