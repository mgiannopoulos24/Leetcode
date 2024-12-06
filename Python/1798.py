from typing import List

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # Step 1: Sort the coins
        coins.sort()
        
        # Step 2: Initialize reachable range
        reachable = 0
        
        # Step 3: Extend reachable range using each coin
        for coin in coins:
            if coin > reachable + 1:
                break
            reachable += coin
            
        # Step 4: Return the maximum number of consecutive values achievable starting from 0
        return reachable + 1
