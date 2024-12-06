class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Function to calculate the number of moves to ensure that `nums[i]` is greater than its neighbors
        def moves_to_fix(i):
            moves = 0
            if i > 0:
                moves = max(moves, nums[i] - nums[i-1] + 1)
            if i < n - 1:
                moves = max(moves, nums[i] - nums[i+1] + 1)
            return moves
        
        # Case 1: Even-indexed elements should be larger than their neighbors
        even_moves = 0
        for i in range(0, n, 2):
            even_moves += moves_to_fix(i)
        
        # Case 2: Odd-indexed elements should be larger than their neighbors
        odd_moves = 0
        for i in range(1, n, 2):
            odd_moves += moves_to_fix(i)
        
        # Return the minimum number of moves for either pattern
        return min(even_moves, odd_moves)
