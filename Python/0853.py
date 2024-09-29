from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Compute time to reach the target for each car
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - pos) / spd for pos, spd in cars]
        
        # Step 2: Count the number of fleets
        fleets = 0
        current_max_time = 0
        
        for time in times:
            if time > current_max_time:
                fleets += 1
                current_max_time = time
        
        return fleets
