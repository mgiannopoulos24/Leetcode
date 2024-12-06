from typing import List

class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10**9 +7
        n = len(s)
        max_n = n

        # Precompute factorial and inverse factorial
        fact = [1] * (max_n +1)
        for i in range(1, max_n +1):
            fact[i] = (fact[i-1] * i) % MOD

        # Compute inverse factorial using Fermat's Little Theorem
        inv_fact = [1] * (max_n +1)
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n -1, -1, -1):
            inv_fact[i] = (inv_fact[i+1] * (i+1)) % MOD

        # Frequency of each character
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] +=1

        rank =0
        for i in range(n):
            c = ord(s[i]) - ord('a')
            # For all characters less than c
            for smaller in range(0, c):
                if freq[smaller] ==0:
                    continue
                # Choose 'smaller' character at position i
                freq[smaller] -=1
                # Calculate number of unique permutations with remaining characters
                perms = fact[n - i -1]
                for f in freq:
                    perms = (perms * inv_fact[f]) % MOD
                rank = (rank + perms) % MOD
                # Restore frequency
                freq[smaller] +=1
            # Fix the current character
            freq[c] -=1
            if freq[c] <0:
                # This should not happen
                return 0

        # Rank is 1-based
        operations = (rank) % MOD
        return operations
