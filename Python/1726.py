from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Dictionary to store pairs with the same product
        product_map = defaultdict(int)
        
        # Step 1: Calculate product of every unique pair and store in product_map
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product] += 1
        
        # Step 2: Calculate number of tuples for each product
        total_tuples = 0
        for count in product_map.values():
            if count > 1:
                total_tuples += count * (count - 1) * 4  # each valid pair contributes 4 tuples
        
        return total_tuples
