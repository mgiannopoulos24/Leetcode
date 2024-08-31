from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # `write_index` will point to the index where the next valid element will be written
        write_index = 1
        # Counter for the occurrences of the current element
        count = 1
        
        # Start from the second element
        for i in range(1, len(nums)):
            # If the current element is the same as the previous one
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            # Write the element to `write_index` if the count is less than or equal to 2
            if count <= 2:
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index