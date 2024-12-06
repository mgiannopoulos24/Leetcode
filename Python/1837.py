class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # Initialize the sum of digits to zero
        digit_sum = 0
        
        # Convert `n` to base `k` and sum the digits
        while n > 0:
            digit_sum += n % k
            n //= k
        
        return digit_sum
