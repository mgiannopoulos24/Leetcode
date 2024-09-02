from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Quick lookup for stone positions
        stone_positions = set(stones)
        
        # Dictionary to keep track of reachable states
        dp = {stone: set() for stone in stones}
        dp[stones[0]].add(0)
        
        for stone in stones:
            for last_jump in dp[stone]:
                # Try jumps of length last_jump - 1, last_jump, and last_jump + 1
                for d in [-1, 0, 1]:
                    next_jump = last_jump + d
                    if next_jump > 0:
                        next_position = stone + next_jump
                        if next_position in stone_positions:
                            dp[next_position].add(next_jump)
        
        # If the last stone has any entries in dp, return True, otherwise False
        return bool(dp[stones[-1]])

