from typing import List

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Sort rides based on the end point
        rides.sort(key=lambda x: x[1])
        
        # Initialize dp array
        dp = [0] * (n + 1)
        
        # Initialize a pointer for the rides
        ride_index = 0
        
        for i in range(1, n + 1):
            # Carry over the previous maximum earnings
            dp[i] = dp[i - 1]
            
            # Process all rides that end at the current point
            while ride_index < len(rides) and rides[ride_index][1] == i:
                start, end, tip = rides[ride_index]
                # Calculate the earnings if we take this ride
                current_earning = (end - start) + tip + dp[start]
                # Update the dp array if this ride gives more earnings
                dp[i] = max(dp[i], current_earning)
                ride_index += 1
        
        return dp[n]