from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        PHI_MOD = 1140  # Euler's totient function value for 1337
        
        def mod_exp(base: int, exp: int, mod: int) -> int:
            result = 1
            base %= mod
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
        
        # Convert b array to an integer modulo PHI_MOD
        exp_mod = 0
        for digit in b:
            exp_mod = (exp_mod * 10 + digit) % PHI_MOD
        
        # Handle the case where the exponent is zero
        if exp_mod == 0:
            exp_mod = PHI_MOD
        
        # Compute (a^exp_mod) % MOD
        return mod_exp(a, exp_mod, MOD)
