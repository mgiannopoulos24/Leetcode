from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Apply the operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Step 2: Shift all zeros to the end
        # We can do this by creating a new list that contains all non-zero elements first, followed by zeros
        result = []
        zero_count = 0
        
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                zero_count += 1
        
        # Append the zeros at the end
        result.extend([0] * zero_count)
        
        return result