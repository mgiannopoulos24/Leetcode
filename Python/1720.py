from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # Initialize the original array with the first element
        arr = [first]
        
        # Reconstruct the original array
        for i in range(len(encoded)):
            # Compute the next element by XORing the last element in arr with encoded[i]
            arr.append(arr[-1] ^ encoded[i])
        
        return arr
