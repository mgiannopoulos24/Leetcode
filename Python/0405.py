class Solution:
    def toHex(self, num: int) -> str:
        # Hexadecimal digit characters
        hex_chars = "0123456789abcdef"
        
        # Handle the case for zero directly
        if num == 0:
            return "0"
        
        # Handle negative numbers using two's complement for 32-bit integers
        if num < 0:
            num += 2**32
        
        # Convert number to hexadecimal
        result = []
        while num > 0:
            remainder = num % 16
            result.append(hex_chars[remainder])
            num //= 16
        
        # The result array contains the hexadecimal digits in reverse order
        return ''.join(reversed(result))
