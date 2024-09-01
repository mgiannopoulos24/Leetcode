class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize a list to track prime numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Start marking non-prime numbers
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
        
        # Count the primes
        return sum(is_prime)
