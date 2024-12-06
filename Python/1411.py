class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initial counts for the first row
        A = 6  # Type ABC
        B = 6  # Type ABA
        
        for i in range(2, n + 1):
            new_A = (2 * A + 2 * B) % MOD
            new_B = (2 * A + 3 * B) % MOD
            A, B = new_A, new_B
        
        return (A + B) % MOD