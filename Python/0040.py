from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()  # Sort candidates to handle duplicates
        
        def backtrack(current_combination, start, target):
            if target == 0:
                results.append(list(current_combination))
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                if candidates[i] > target:
                    break  # No need to check further since candidates is sorted
                
                current_combination.append(candidates[i])
                backtrack(current_combination, i + 1, target - candidates[i])
                current_combination.pop()
        
        backtrack([], 0, target)
        return results
