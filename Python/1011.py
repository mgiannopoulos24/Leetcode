from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper function to check if we can ship all packages within 'days' using 'capacity'
        def canShipWithCapacity(capacity):
            current_weight = 0
            required_days = 1  # We need at least one day to ship
            for weight in weights:
                # If adding this package exceeds the capacity, we need a new day
                if current_weight + weight > capacity:
                    required_days += 1
                    current_weight = 0  # Start a new day with the current package
                current_weight += weight
            return required_days <= days

        # Binary search for the minimum possible capacity
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShipWithCapacity(mid):
                right = mid  # Try to find a smaller feasible capacity
            else:
                left = mid + 1  # Increase the capacity since it's not feasible
        
        return left
