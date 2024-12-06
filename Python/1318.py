class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        # Iterate through each bit
        while a > 0 or b > 0 or c > 0:
            # Extract the least significant bits of a, b, and c
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1
            
            # Case 1: If c_bit is 1, either a_bit or b_bit must be 1
            if c_bit == 1:
                if a_bit == 0 and b_bit == 0:
                    flips += 1  # We need to flip either a or b to 1
            # Case 2: If c_bit is 0, both a_bit and b_bit must be 0
            else:
                if a_bit == 1:
                    flips += 1  # Flip a's bit to 0
                if b_bit == 1:
                    flips += 1  # Flip b's bit to 0
            
            # Right shift to move to the next bit
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips
