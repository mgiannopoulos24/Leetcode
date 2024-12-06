class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Step 1: Sort the piles in descending order
        piles.sort(reverse=True)
        
        # Step 2: Initialize the total coins to collect
        total_coins = 0
        
        # Step 3: Pick the second-largest pile in each triplet
        n = len(piles) // 3
        for i in range(1, 2 * n, 2):  # We start at index 1 and skip every second pile (Bob's pile)
            total_coins += piles[i]
        
        return total_coins
