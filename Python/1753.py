class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # Sort the piles so that a <= b <= c
        a, b, c = sorted([a, b, c])
        
        # Use the minimum of (total stones // 2) or (a + b) for the maximum score
        return min(a + b, (a + b + c) // 2)
