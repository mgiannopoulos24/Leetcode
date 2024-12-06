import math

MOD = 10**9 + 7

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # Helper function to check if a number is prime
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        
        # Step 1: Count primes in the range 1 to n
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        non_prime_count = n - prime_count
        
        # Step 2: Calculate the factorial of prime_count and non_prime_count
        prime_fact = math.factorial(prime_count) % MOD
        non_prime_fact = math.factorial(non_prime_count) % MOD
        
        # Step 3: Multiply them and return the result modulo 10^9 + 7
        return (prime_fact * non_prime_fact) % MOD
