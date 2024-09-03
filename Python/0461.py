class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Compute XOR of x and y
        xor = x ^ y
        
        # Count the number of 1s in the binary representation of the XOR result
        return bin(xor).count('1')
