from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort box types by units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        
        for numberOfBoxes, unitsPerBox in boxTypes:
            if truckSize <= 0:
                break  # Stop if there's no more room on the truck
            
            # Calculate how many boxes to take from this type
            boxes_to_take = min(numberOfBoxes, truckSize)
            
            # Add units from these boxes to the total
            total_units += boxes_to_take * unitsPerBox
            
            # Decrease remaining truck capacity
            truckSize -= boxes_to_take
        
        return total_units
