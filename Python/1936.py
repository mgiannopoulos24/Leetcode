from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        current_height = 0
        additional_rungs = 0
        
        for rung in rungs:
            gap = rung - current_height
            if gap > dist:
                # Calculate the number of additional rungs needed
                additional_rungs += (gap - 1) // dist
            current_height = rung
        
        return additional_rungs
