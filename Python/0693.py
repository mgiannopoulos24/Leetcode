class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Perform the XOR operation
        x = n ^ (n >> 1)
        # Check if x is of the form 111...1
        return (x & (x + 1)) == 0
