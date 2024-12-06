from typing import List

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Computes the XOR sum of all (arr1[i] & arr2[j]) for all i, j.
        Utilizes the property that XOR over ANDs can be simplified as:
        (XOR of arr1) & (XOR of arr2)
        """
        # Compute XOR of all elements in arr1
        arr1_xor = 0
        for num in arr1:
            arr1_xor ^= num
                    
        # Compute XOR of all elements in arr2
        arr2_xor = 0
        for num in arr2:
            arr2_xor ^= num
                    
        # Compute the final XOR sum using the simplification
        result = arr1_xor & arr2_xor
        
        return result
