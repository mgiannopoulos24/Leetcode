class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Find the bit length of the number
        bit_length = num.bit_length()
        
        # Step 2: Create a bitmask of the same length where all bits are 1
        bitmask = (1 << bit_length) - 1
        
        # Step 3: XOR the number with the bitmask to get the complement
        return num ^ bitmask
