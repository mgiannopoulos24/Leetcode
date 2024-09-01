class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for _ in range(32):
            # Shift reversed_n to the left to make room for the new bit
            reversed_n <<= 1
            # Add the least significant bit of n to reversed_n
            reversed_n |= (n & 1)
            # Shift n to the right to process the next bit
            n >>= 1
        return reversed_n
