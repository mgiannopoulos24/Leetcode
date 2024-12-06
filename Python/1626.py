class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # Combine scores and ages, and then sort them by age first and then by score
        players = sorted(zip(ages, scores))
        
        n = len(scores)
        dp = [0] * n  # dp[i] will store the best score possible including player i
        
        # Initialize dp: each player's best score can at least be their own score
        for i in range(n):
            dp[i] = players[i][1]  # The score of the ith player after sorting
        
        # Fill dp array
        for i in range(n):
            for j in range(i):
                if players[j][1] <= players[i][1]:  # No conflict, so we can add j to the team
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        
        return max(dp)
