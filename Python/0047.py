from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
                return
            
            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                
                visited[i] = True
                permutation.append(nums[i])
                backtrack()
                permutation.pop()
                visited[i] = False
        
        permutations = []
        permutation = []
        visited = [False] * len(nums)
        nums.sort()
        backtrack()
        return permutations
