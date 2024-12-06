from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # Variable to store the closest cost found
        closest = float('inf')
        
        # Helper function for recursive DFS
        def dfs(current_cost, index):
            nonlocal closest
            
            # Update the closest cost if this one is closer to the target
            if abs(current_cost - target) < abs(closest - target) or \
               (abs(current_cost - target) == abs(closest - target) and current_cost < closest):
                closest = current_cost
            
            # Early exit if current cost exceeds the target + the closest difference so far
            if current_cost >= target or index == len(toppingCosts):
                return
            
            # Try adding 0, 1, or 2 of the current topping
            dfs(current_cost, index + 1)                 # No topping
            dfs(current_cost + toppingCosts[index], index + 1)   # Add one topping
            dfs(current_cost + 2 * toppingCosts[index], index + 1)  # Add two toppings
        
        # Try each base cost and explore topping combinations
        for base in baseCosts:
            dfs(base, 0)
        
        return closest
