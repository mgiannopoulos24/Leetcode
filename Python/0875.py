from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAllBananas(k: int) -> bool:
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / k)
                if hours_needed > h:
                    return False
            return hours_needed <= h
        
        # Binary search for the minimum k
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if canEatAllBananas(mid):
                right = mid  # Try a smaller k
            else:
                left = mid + 1  # Increase k
        
        return left
