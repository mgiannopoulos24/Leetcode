from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zeros_count = 0
        
        # Sliding window: expand the window by moving `right`
        for right in range(len(nums)):
            # If we encounter a 0, increment the zeros count
            if nums[right] == 0:
                zeros_count += 1
            
            # If the number of zeros exceeds k, shrink the window from the left
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1  # Move the left pointer
            
            # Calculate the current window size and update the maximum length
            max_len = max(max_len, right - left + 1)
        
        return max_len
