from bisect import bisect_left
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Sort the houses and heaters
        houses.sort()
        heaters.sort()
        
        def find_closest_distance(house: int) -> int:
            # Binary search for the position to insert the house in the heaters list
            pos = bisect_left(heaters, house)
            
            # If house is before the first heater or after the last heater
            if pos == 0:
                return abs(house - heaters[0])
            if pos == len(heaters):
                return abs(house - heaters[-1])
            
            # Calculate distance to the closest heaters on both sides
            left_distance = abs(house - heaters[pos - 1])
            right_distance = abs(house - heaters[pos])
            
            return min(left_distance, right_distance)
        
        # Find the maximum distance for all houses to be covered
        return max(find_closest_distance(house) for house in houses)
