class Solution:
    def divisorGame(self, n: int) -> bool:
        # Alice wins if n is even, otherwise Bob wins
        return n % 2 == 0
