from typing import List
import math

MOD = 10**9 + 7
MAX = 20000  # Increase MAX to handle larger values

# Precompute factorials and modular inverses up to MAX
factorial = [1] * (MAX + 1)
inverse_factorial = [1] * (MAX + 1)

# Populate factorial and inverse factorial arrays
for i in range(2, MAX + 1):
    factorial[i] = factorial[i - 1] * i % MOD

# Modular exponentiation to find modular inverse of factorial[MAX] under MOD
inverse_factorial[MAX] = pow(factorial[MAX], MOD - 2, MOD)
for i in range(MAX - 1, 0, -1):
    inverse_factorial[i] = inverse_factorial[i + 1] * (i + 1) % MOD
inverse_factorial[0] = 1  # By definition

# Binomial coefficient function under modulo with bounds checking
def binomial(n, k):
    if n < k or k < 0:
        return 0
    if n > MAX:  # Dynamically compute factorial if beyond precomputed range
        num = 1
        for i in range(n - k + 1, n + 1):
            num = num * i % MOD
        denom = 1
        for i in range(1, k + 1):
            denom = denom * i % MOD
        return num * pow(denom, MOD - 2, MOD) % MOD
    return factorial[n] * inverse_factorial[k] % MOD * inverse_factorial[n - k] % MOD

# Function to factorize a number and return its prime factors with their counts
def prime_factors(x):
    factors = []
    d = 2
    while d * d <= x:
        count = 0
        while (x % d) == 0:
            x //= d
            count += 1
        if count > 0:
            factors.append((d, count))
        d += 1
    if x > 1:
        factors.append((x, 1))
    return factors

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        result = []
        
        for n, k in queries:
            ways = 1
            for prime, exponent in prime_factors(k):
                ways *= binomial(exponent + n - 1, exponent)
                ways %= MOD
            result.append(ways)
        
        return result
