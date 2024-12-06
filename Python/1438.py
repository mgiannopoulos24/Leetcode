from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()  # To store indices of maximum elements in window
        min_deque = deque()  # To store indices of minimum elements in window
        left = 0  # Left pointer of the window
        max_len = 0
        
        # Traverse the array with the right pointer
        for right in range(len(nums)):
            # Maintain the max deque (store in decreasing order)
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain the min deque (store in increasing order)
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Check if the current window satisfies the condition
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                # Shrink the window from the left
                left += 1
                # Remove elements outside of the window in both deques
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update the maximum length of the valid window
            max_len = max(max_len, right - left + 1)
        
        return max_len