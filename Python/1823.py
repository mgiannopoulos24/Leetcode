class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner_position = 0  # base case for J(1, k)
        
        # Iteratively apply the recurrence relation for n friends
        for i in range(2, n + 1):
            winner_position = (winner_position + k) % i
        
        # Convert zero-based index to one-based index
        return winner_position + 1
