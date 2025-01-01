from itertools import combinations

class Solution:
    def maxProduct(self, s: str) -> int:
        def is_palindrome(subseq):
            return subseq == subseq[::-1]

        n = len(s)
        max_product = 0
        
        # Generate all possible subsets of indices
        for mask1 in range(1, 1 << n):
            # Subsequence from the first mask
            subseq1 = ''.join(s[i] for i in range(n) if mask1 & (1 << i))
            if not is_palindrome(subseq1):
                continue
            
            # Generate complementary subsets for the second subsequence
            for mask2 in range(1, 1 << n):
                if mask1 & mask2 == 0:  # Ensure disjoint subsequences
                    subseq2 = ''.join(s[i] for i in range(n) if mask2 & (1 << i))
                    if is_palindrome(subseq2):
                        max_product = max(max_product, len(subseq1) * len(subseq2))
        
        return max_product
