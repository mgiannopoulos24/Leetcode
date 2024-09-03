from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Initialize a hash map to store the first occurrence of each prefix sum
        prefix_sum_index = {0: -1}  # Handle the case where the subarray starts from index 0
        max_length = 0
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            # Update prefix_sum: Convert 0 to -1 and add to the current prefix_sum
            prefix_sum += 1 if num == 1 else -1
            
            # Check if this prefix_sum has been seen before
            if prefix_sum in prefix_sum_index:
                # Calculate the length of the subarray
                length = i - prefix_sum_index[prefix_sum]
                max_length = max(max_length, length)
            else:
                # Store the first occurrence of this prefix_sum
                prefix_sum_index[prefix_sum] = i
        
        return max_length
