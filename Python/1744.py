from typing import List
from itertools import accumulate

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # Step 1: Compute prefix sums for cumulative candy counts
        prefix_sum = list(accumulate(candiesCount))
        
        # Step 2: Initialize the result list
        result = []
        
        # Step 3: Process each query
        for favoriteType, favoriteDay, dailyCap in queries:
            # Calculate the total number of candies up to the previous type
            min_candies_needed = favoriteDay + 1
            max_candies_possible = (favoriteDay + 1) * dailyCap
            
            # Calculate the range of candies for favoriteType
            total_candies_before = prefix_sum[favoriteType - 1] if favoriteType > 0 else 0
            total_candies_for_type = prefix_sum[favoriteType]
            
            # Check if there is any overlap in the range of candies you could consume
            can_eat = not (max_candies_possible <= total_candies_before or min_candies_needed > total_candies_for_type)
            
            # Append the result
            result.append(can_eat)
        
        return result
