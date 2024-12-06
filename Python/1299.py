from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        greatest = -1
        
        # Traverse the array from the end to the start
        for i in range(n - 1, -1, -1):
            new_val = greatest
            greatest = max(greatest, arr[i])
            arr[i] = new_val
            
        return arr
