class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit integer limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Initialize variables
        result = 0
        sign = 1
        i = 0
        
        # Skip leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Handle sign
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Convert digits
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow before adding new digit
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1
        
        # Apply sign
        result *= sign
        
        # Ensure result is within the 32-bit integer range
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        
        return result
