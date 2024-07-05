class Solution:
    def reverse(self, x: int) -> int:
        # Define the limits of a 32-bit signed integer
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Initialize variables for storing the reversed number and handle negative sign
        reversed_x = 0
        is_negative = x < 0
        x = abs(x)
        
        # Reverse the digits of x
        while x != 0:
            # Extract the last digit
            digit = x % 10
            # Append it to reversed_x
            reversed_x = reversed_x * 10 + digit
            # Remove the last digit from x
            x //= 10
        
        # Apply the sign to reversed_x if the original number was negative
        if is_negative:
            reversed_x = -reversed_x
        
        # Check for integer overflow and return 0 if out of bounds
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x
