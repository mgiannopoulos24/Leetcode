from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Sort the array to simplify checking divisibility
        nums.sort()
        n = len(nums)

        # dp[i] will store the length of the largest subset ending with nums[i]
        dp = [1] * n
        # previous[i] will store the index of the previous element in the subset
        previous = [-1] * n
        
        # Variables to keep track of the maximum subset length and its end index
        max_len = 0
        max_index = 0

        for j in range(1, n):
            for i in range(j):
                if nums[j] % nums[i] == 0:
                    if dp[i] + 1 > dp[j]:
                        dp[j] = dp[i] + 1
                        previous[j] = i
            if dp[j] > max_len:
                max_len = dp[j]
                max_index = j

        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = previous[max_index]
        
        # The result needs to be reversed as we constructed it backwards
        return result[::-1]
