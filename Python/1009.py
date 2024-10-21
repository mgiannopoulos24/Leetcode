class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Special case for n = 0
        if n == 0:
            return 1
        
        # Find the mask that has the same number of bits as n and is all 1's
        # Example: if n = 5 (which is '101'), mask will be '111' (7 in decimal)
        mask = (1 << n.bit_length()) - 1
        
        # XOR n with the mask to flip all bits
        return n ^ mask
