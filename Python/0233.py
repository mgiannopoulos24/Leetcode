class Solution:
    def countDigitOne(self, n: int) -> int:
        # Count of ones at each digit position
        count = 0
        factor = 1  # Position factor (units, tens, hundreds, etc.)
        
        while factor <= n:
            lower_numbers = n - (n // factor) * factor
            current_digit = (n // factor) % 10
            higher_numbers = n // (factor * 10)
            
            # Counting based on the current digit
            if current_digit == 0:
                count += higher_numbers * factor
            elif current_digit == 1:
                count += higher_numbers * factor + lower_numbers + 1
            else:
                count += (higher_numbers + 1) * factor
            
            # Move to the next digit position
            factor *= 10
        
        return count
