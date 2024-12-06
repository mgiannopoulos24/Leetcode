from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        
        # Traverse the matrix and collect elements by their diagonal index i + j
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])
        
        # We need to traverse the diagonals in the order of their sum i + j
        result = []
        for k in sorted(diagonals.keys()):
            # Reverse the elements because we want to traverse each diagonal from top-right to bottom-left
            result.extend(diagonals[k][::-1])
        
        return result