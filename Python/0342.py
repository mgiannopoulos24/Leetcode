class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is greater than 0 and is a power of two
        if n <= 0:
            return False
        
        # Check if n is a power of two
        if (n & (n - 1)) != 0:
            return False
        
        # Check if the single bit is in the correct position for power of four
        # A number that is power of four has exactly one bit set and that bit must be in position 0, 2, 4, 6, etc.
        # We can use (n & 0x55555555) to test if the bit is in one of these positions
        return (n & 0x55555555) != 0
