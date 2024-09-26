from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n - 1:
            if bits[i] == 1:
                i += 2  # Skip the next bit since current '1' and next '0' or '1' form a two-bit character
            else:
                i += 1  # Move to the next bit
        
        # If we ended up at the last bit position, it's a valid one-bit character
        return i == n - 1