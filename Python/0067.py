class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        int_a = int(a, 2)
        int_b = int(b, 2)
        
        # Add the integers
        sum_int = int_a + int_b
        
        # Convert the sum back to a binary string
        # bin() function returns a binary string prefixed with '0b', so we slice off the first two characters
        return bin(sum_int)[2:]
