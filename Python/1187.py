from typing import List
from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Returns the minimum number of operations needed to make arr1 strictly increasing.
        In one operation, you can replace any element in arr1 with any element from arr2.
        If it's impossible, returns -1.
        
        Args:
        arr1 (List[int]): The original array.
        arr2 (List[int]): The array from which elements can be used for replacement.
        
        Returns:
        int: The minimum number of operations required or -1 if impossible.
        """
        
        # Step 1: Preprocess arr2
        arr2 = sorted(list(set(arr2)))  # Sort and remove duplicates for binary search
        
        n = len(arr1)
        
        # Initialize DP dictionary
        # Key: last number of the increasing sequence
        # Value: minimum number of operations to reach this state
        dp = { -1: 0 }  # Start with a dummy number less than any possible number
        
        for i in range(n):
            current = arr1[i]
            temp = {}
            for last, operations in dp.items():
                # Option 1: Keep the current number if it's greater than the last number
                if current > last:
                    if current in temp:
                        temp[current] = min(temp[current], operations)
                    else:
                        temp[current] = operations
                
                # Option 2: Replace the current number with the smallest number in arr2 > last
                idx = bisect_right(arr2, last)
                if idx < len(arr2):
                    replacement = arr2[idx]
                    if replacement in temp:
                        temp[replacement] = min(temp[replacement], operations + 1)
                    else:
                        temp[replacement] = operations + 1
            
            # Update dp with the new states from temp
            dp = temp
            
            # Early termination: If no possible states, return -1
            if not dp:
                return -1
        
        # Return the minimum operations from the final dp states
        return min(dp.values()) if dp else -1