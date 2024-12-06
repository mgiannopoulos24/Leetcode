from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # Step 1: Sort the array to find the median
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        
        # Step 2: Sort by strength and value (in descending order)
        def strength(x):
            return (abs(x - median), x)
        
        # Sort by strength (abs difference to median, and by value in descending order)
        arr.sort(key=lambda x: (abs(x - median), x), reverse=True)
        
        # Step 3: Return the first k elements
        return arr[:k]
