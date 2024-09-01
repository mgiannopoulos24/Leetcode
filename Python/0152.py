from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize variables
        max_product = min_product = result = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Compute potential new max and min products
            temp_max = max(num, num * max_product, num * min_product)
            min_product = min(num, num * max_product, num * min_product)
            
            # Update max_product with the highest of the computed values
            max_product = temp_max
            
            # Update the result with the maximum product found so far
            result = max(result, max_product)
        
        return result
