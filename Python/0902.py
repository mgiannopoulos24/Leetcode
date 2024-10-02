from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        S = str(n)
        K = len(S)
        digits_len = len(digits)
        
        # Step 1: Count numbers with digits less than the length of n
        count = 0
        for i in range(1, K):
            count += digits_len ** i

        # Step 2: Count numbers with exactly the same number of digits as n
        for i in range(K):
            has_same_prefix = False
            for d in digits:
                if d < S[i]:
                    count += digits_len ** (K - i - 1)
                elif d == S[i]:
                    has_same_prefix = True
            
            if not has_same_prefix:
                return count
        
        return count + 1