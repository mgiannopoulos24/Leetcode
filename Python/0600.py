class Solution:
    def findIntegers(self, n: int) -> int:
        # Build the dp table for valid numbers
        dp = [0] * 32
        dp[0] = 1  # Base case: 1 valid number with 0 bits (empty number)
        dp[1] = 2  # Base case: 2 valid numbers with 1 bit (0 and 1)
        
        # Fill the dp table
        for i in range(2, 32):
            dp[i] = dp[i-1] + dp[i-2]
        
        # Traverse bits of n to count valid numbers
        count = 0
        prev_bit = 0  # Track the previous bit to avoid consecutive ones
        
        for i in range(31, -1, -1):
            if (n >> i) & 1:
                count += dp[i]
                if prev_bit:
                    return count
                prev_bit = 1
            else:
                prev_bit = 0
        
        return count + 1
