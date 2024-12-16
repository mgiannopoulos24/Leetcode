from typing import List

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Initialize prefix sum array for numbers 1 to 100
        max_val = 100
        n = len(nums)
        freq = [[0] * (max_val + 1) for _ in range(n + 1)]

        # Build the prefix sum array
        for i in range(n):
            for j in range(1, max_val + 1):
                freq[i + 1][j] = freq[i][j] + (1 if nums[i] == j else 0)

        # Result array
        res = []

        # Process each query
        for li, ri in queries:
            # Find all numbers in the range [li, ri]
            present = []
            for num in range(1, max_val + 1):
                if freq[ri + 1][num] - freq[li][num] > 0:
                    present.append(num)

            # Compute the minimum absolute difference
            if len(present) < 2:
                res.append(-1)
            else:
                min_diff = float('inf')
                for i in range(1, len(present)):
                    min_diff = min(min_diff, present[i] - present[i - 1])
                res.append(min_diff)

        return res
