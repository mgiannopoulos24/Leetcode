class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()  # Sort the positions of the stones
        n = len(stones)
        
        # Maximum moves calculation
        max_moves = max(stones[-1] - stones[1] - (n - 2), stones[-2] - stones[0] - (n - 2))
        
        # Minimum moves calculation using sliding window
        min_moves = float('inf')
        j = 0
        
        for i in range(n):
            while j < n and stones[j] - stones[i] + 1 <= n:
                j += 1
            already_in_window = j - i
            if already_in_window == n - 1 and stones[j - 1] - stones[i] + 1 == n - 1:
                # Handle the special case where we have n-1 consecutive stones and a gap
                # Moving one of the two endpoints will only take 2 moves instead of 1
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - already_in_window)
        
        return [min_moves, max_moves]
