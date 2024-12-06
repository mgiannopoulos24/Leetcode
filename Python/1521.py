from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        prev_ands = set()
        min_diff = float('inf')
        
        for index, num in enumerate(arr):
            current_ands = set()
            
            # Update the set with bitwise AND of current number with all previous ANDs
            for prev_and in prev_ands:
                current_and = prev_and & num
                current_ands.add(current_and)
                # Update min_diff
                diff = abs(current_and - target)
                if diff < min_diff:
                    min_diff = diff
            
            # Include the current number itself as a subarray of length 1
            current_ands.add(num)
            diff = abs(num - target)
            if diff < min_diff:
                min_diff = diff
            
            # Update prev_ands for the next iteration
            prev_ands = current_ands
        
        return min_diff
