from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == n:
                permutations.append(nums[:])
                return
            
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        
        permutations = []
        n = len(nums)
        backtrack(0)
        return permutations
