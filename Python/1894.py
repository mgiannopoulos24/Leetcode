from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Calculate the total amount of chalk needed for one full cycle
        total_chalk = sum(chalk)
        
        # Calculate the remaining chalk after full cycles
        remaining_chalk = k % total_chalk
        
        # Find the student that will replace the chalk
        for i, chalk_needed in enumerate(chalk):
            if remaining_chalk < chalk_needed:
                return i
            remaining_chalk -= chalk_needed
        
        # If not found (shouldn't happen with correct input), return -1
        return -1
