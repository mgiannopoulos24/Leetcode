from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        total_odds = 0
        even_count = 1  # Prefix sum of 0 is even
        odd_count = 0
        current_sum = 0

        for index, num in enumerate(arr):
            current_sum += num
            if current_sum % 2 == 0:
                # Current prefix sum is even
                total_odds = (total_odds + odd_count) % MOD
                even_count += 1
            else:
                # Current prefix sum is odd
                total_odds = (total_odds + even_count) % MOD
                odd_count += 1

        return total_odds
