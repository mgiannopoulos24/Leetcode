class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert number to a list of digits
        digits = list(str(num))
        
        # Record the last index of each digit
        last_index = {int(digit): i for i, digit in enumerate(digits)}
        
        # Traverse the digits to find the first place where a swap would be beneficial
        for i, digit in enumerate(digits):
            # Check digits greater than the current one from right to left
            for d in range(9, int(digit), -1):
                if d in last_index and last_index[d] > i:
                    # Swap the current digit with the largest possible digit
                    digits[i], digits[last_index[d]] = digits[last_index[d]], digits[i]
                    # Convert back to integer and return
                    return int(''.join(digits))
        
        # No beneficial swap was found; return the original number
        return num
