from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # If the path has at least two elements, add it to the set
            if len(path) > 1:
                unique_subsequences.add(tuple(path))
            
            # Use a set to avoid picking the same element more than once in the same position
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
        
        unique_subsequences = set()
        backtrack(0, [])
        return list(map(list, unique_subsequences))
