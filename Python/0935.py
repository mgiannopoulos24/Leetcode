class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Possible moves from each digit
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],      # No valid knight moves from 5
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        # Initialize dp with base case: dp[0][digit] = 1 for each digit
        dp = [1] * 10
        
        # Iterate for each step from 1 to n-1
        for step in range(1, n):
            new_dp = [0] * 10
            for digit in range(10):
                for next_digit in moves[digit]:
                    new_dp[next_digit] = (new_dp[next_digit] + dp[digit]) % MOD
            dp = new_dp
        
        # The result is the sum of all dp states after n-1 steps
        return sum(dp) % MOD
