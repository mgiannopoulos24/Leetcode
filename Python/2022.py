from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if it's possible to reshape the array
        if len(original) != m * n:
            return []
        
        # Construct the 2D array
        result = []
        for i in range(m):
            # Get the slice for the current row
            start_index = i * n
            end_index = (i + 1) * n
            row = original[start_index:end_index]
            result.append(row)
        
        return result
