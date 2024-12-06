from typing import List

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        # Sort the maximumHeight in descending order
        maximumHeight.sort(reverse=True)
        
        total_sum = 0
        prev_height = float('inf')  # Initialize previous height as infinity
        
        for height in maximumHeight:
            # Assign the current height as the minimum of the current maximumHeight and (prev_height - 1)
            assigned_height = min(height, prev_height - 1)
            
            # If the assigned height is less than 1, it's impossible to assign unique positive heights
            if assigned_height <= 0:
                return -1
            
            # Add the assigned height to the total sum
            total_sum += assigned_height
            
            # Update prev_height for the next iteration
            prev_height = assigned_height
        
        return total_sum