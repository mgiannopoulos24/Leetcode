class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle edge case of overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of the result
        sign = (dividend > 0) == (divisor > 0)
        
        # Convert both numbers to positive to simplify computation
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        while dividend >= divisor:
            divisor_shifted = divisor
            quotient_increment = 1
            while dividend >= (divisor_shifted << 1):
                divisor_shifted <<= 1
                quotient_increment <<= 1
            dividend -= divisor_shifted
            result += quotient_increment
        
        # Apply sign
        if not sign:
            result = -result
        
        # Check for overflow
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result
