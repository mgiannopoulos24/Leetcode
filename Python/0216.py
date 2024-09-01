from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, remaining_k, remaining_sum):
            # Base case: if combination is of size k and sum equals n
            if remaining_k == 0 and remaining_sum == 0:
                result.append(path)
                return
            # If the combination is invalid
            if remaining_k < 0 or remaining_sum < 0:
                return
            
            # Explore further numbers from the current start point
            for num in range(start, 10):
                backtrack(num + 1, path + [num], remaining_k - 1, remaining_sum - num)
        
        result = []
        backtrack(1, [], k, n)
        return result
