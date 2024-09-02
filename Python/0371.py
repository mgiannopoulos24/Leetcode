class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0xFFFFFFFF  # Mask for 32-bit integer
        INT_MAX = 0x7FFFFFFF  # Maximum positive value for 32-bit integer

        while b != 0:
            # Calculate carry and shift it left by 1 bit
            carry = a & b
            carry <<= 1

            # Calculate sum without carry
            a = (a ^ b) & MAX  # Apply mask to simulate 32-bit integer overflow

            # Update b to be the carry
            b = carry

        # Handle negative values (convert result to signed 32-bit integer)
        return a if a <= INT_MAX else ~(a ^ MAX)
