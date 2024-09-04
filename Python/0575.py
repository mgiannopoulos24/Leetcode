from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Number of candies Alice can eat
        n = len(candyType)
        max_eat = n // 2
        
        # Determine the number of unique candy types
        unique_candies = len(set(candyType))
        
        # The result is the minimum of the number of unique candy types and the number of candies Alice can eat
        return min(max_eat, unique_candies)
