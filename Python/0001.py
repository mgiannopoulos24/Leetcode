from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the number and its index
        num_to_index = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement that would sum to the target
            complement = target - num
            
            # If the complement is found in the dictionary, return the indices
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Otherwise, add the number and its index to the dictionary
            num_to_index[num] = i
