class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Edge case: Handle division by zero (though problem guarantees denominator != 0)
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        # Determine the sign of the result
        if numerator * denominator < 0:
            sign = -1
        else:
            sign = 1
        
        # Use absolute values to simplify calculations
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Calculate the integer part
        integer_part = numerator // denominator
        remainder = numerator % denominator
        
        if remainder == 0:
            return f"{'-' * (sign == -1)}{integer_part}"
        
        # Calculate the fractional part
        result = []
        result.append(f"{'-' * (sign == -1)}{integer_part}.")
        
        remainder_map = {}
        decimal_part = []
        
        while remainder != 0:
            # Check if the remainder is repeating
            if remainder in remainder_map:
                repeat_index = remainder_map[remainder]
                decimal_part.insert(repeat_index, '(')
                decimal_part.append(')')
                break
            
            # Record the position of the remainder
            remainder_map[remainder] = len(decimal_part)
            
            # Perform the long division step
            remainder *= 10
            decimal_part.append(str(remainder // denominator))
            remainder %= denominator
        
        return ''.join(result + decimal_part)
