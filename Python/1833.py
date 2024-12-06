from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Find the maximum cost to determine the size of the counting array
        max_cost = max(costs) if costs else 0
        count = [0] * (max_cost + 1)
        
        # Populate the frequency array
        for cost in costs:
            count[cost] += 1
        
        total = 0  # Total ice creams bought
        
        # Iterate through the costs in ascending order
        for c in range(1, max_cost + 1):
            if count[c] == 0:
                continue  # No ice creams at this cost
            if c > coins:
                break  # Cannot afford any more ice creams
            
            # Determine how many ice creams can be bought at this cost
            max_buy = min(count[c], coins // c)
            total += max_buy
            coins -= c * max_buy
            
            if coins == 0:
                break  # No more coins left
        
        return total
