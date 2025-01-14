from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a 1D list
        flattened = []
        for row in grid:
            flattened.extend(row)
        
        # Check if all elements are congruent modulo x
        mod = flattened[0] % x
        for num in flattened:
            if num % x != mod:
                return -1
        
        # Sort the flattened list
        flattened.sort()
        
        # Find the median (middle element)
        n = len(flattened)
        median = flattened[n // 2]
        
        # Calculate the total number of operations
        operations = 0
        for num in flattened:
            operations += abs(num - median) // x
        
        return operations