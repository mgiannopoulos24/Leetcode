class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_length = 0
        
        # Sliding window approach
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                
            # Shrink the window until we have at most 1 zero in the window
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Calculate the length of the current window and update max_length
            max_length = max(max_length, right - left)
        
        return max_length
