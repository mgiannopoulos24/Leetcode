class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # Increment count if the least significant bit is 1
            count += n & 1
            # Shift n to the right to process the next bit
            n >>= 1
        return count
