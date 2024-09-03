from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        
        # Check if total length is divisible by 4
        if total_length % 4 != 0:
            return False
        
        side_length = total_length // 4
        # Sort matchsticks in descending order
        matchsticks.sort(reverse=True)
        
        # If the largest matchstick is greater than side_length, it's impossible
        if matchsticks[0] > side_length:
            return False
        
        # Initialize sides to zero
        sides = [0] * 4
        
        def backtrack(index):
            if index == len(matchsticks):
                # If all sides are equal to the side_length, return True
                return sides[0] == sides[1] == sides[2] == sides[3] == side_length
            
            # Try placing matchstick[index] on each side
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                
                # If a matchstick doesn't fit on an empty side, it won't fit on subsequent empty sides either
                if sides[i] == 0:
                    break
            
            return False
        
        return backtrack(0)
