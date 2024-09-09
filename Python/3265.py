from typing import List
from itertools import permutations

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def generate_swaps(num):
            num_str = str(num)
            results = set()
            # Generate all possible swaps
            for i, j in permutations(range(len(num_str)), 2):
                if i != j:
                    swapped = list(num_str)
                    swapped[i], swapped[j] = swapped[j], swapped[i]
                    results.add(int("".join(swapped)))
            return results

        def can_match_by_swapping(num1, num2):
            swaps = generate_swaps(num1)
            return num2 in swaps

        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] or can_match_by_swapping(nums[i], nums[j]) or can_match_by_swapping(nums[j], nums[i]):
                    count += 1
        return count
