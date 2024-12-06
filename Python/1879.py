class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        from functools import lru_cache

        n = len(nums1)

        # Use bitmask to represent subsets of nums2
        @lru_cache(None)
        def dp(index: int, mask: int) -> int:
            if index == n:
                return 0

            min_xor_sum = float('inf')
            for j in range(n):
                if not (mask & (1 << j)):  # Check if nums2[j] is not used
                    xor_sum = (nums1[index] ^ nums2[j]) + dp(index + 1, mask | (1 << j))
                    min_xor_sum = min(min_xor_sum, xor_sum)

            return min_xor_sum

        return dp(0, 0)
