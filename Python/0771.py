class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Create a set of jewels for fast membership checking
        jewel_set = set(jewels)
        
        # Count stones that are jewels
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        
        return count
