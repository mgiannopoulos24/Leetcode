class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Helper function to compute a^b % MOD using binary exponentiation
        def mod_exp(a, b, mod):
            result = 1
            while b > 0:
                if b % 2 == 1:
                    result = (result * a) % mod
                a = (a * a) % mod
                b //= 2
            return result
        
        # Determine number of even and odd positions
        even_positions = (n + 1) // 2  # If n is odd, we have one more even position
        odd_positions = n // 2
        
        # Calculate the result
        even_count = mod_exp(5, even_positions, MOD)
        odd_count = mod_exp(4, odd_positions, MOD)
        
        # The result is the product of the two counts modulo MOD
        return (even_count * odd_count) % MOD
