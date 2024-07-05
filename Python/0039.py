class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start_idx, current_combination, current_sum):
            if current_sum == target:
                result.append(current_combination[:])
                return
            elif current_sum > target:
                return
            
            for i in range(start_idx, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, current_combination, current_sum + candidates[i])
                current_combination.pop()
        
        result = []
        candidates.sort()  # Sort candidates to handle duplicates and simplify backtracking
        backtrack(0, [], 0)
        return result
