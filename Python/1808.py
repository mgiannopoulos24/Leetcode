class Solution:
    MOD = 10**9 + 7
    
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors == 1:
            return 1
        
        # Determine the optimal number of 3s and 2s
        if primeFactors % 3 == 0:
            # All 3s
            return self.mod_exp(3, primeFactors // 3)
        elif primeFactors % 3 == 1:
            # (3^(k-1)) * (2 * 2) when n % 3 == 1
            return (self.mod_exp(3, (primeFactors // 3) - 1) * 4) % self.MOD
        else:
            # (3^k) * 2 when n % 3 == 2
            return (self.mod_exp(3, primeFactors // 3) * 2) % self.MOD
    
    def mod_exp(self, base: int, exp: int) -> int:
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % self.MOD
            base = (base * base) % self.MOD
            exp //= 2
        return result
