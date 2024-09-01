from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # Initialize the result array
        result = [1] * length
        
        # Calculate prefix products
        prefix_product = 1
        for i in range(length):
            result[i] = prefix_product
            prefix_product *= nums[i]
        
        # Calculate suffix products and combine with prefix products
        suffix_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
        
        return result
