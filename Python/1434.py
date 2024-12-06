MOD = 10**9 + 7

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)  # Number of people

        # Create a list of people who like each hat
        hat_to_people = [[] for _ in range(41)]  # hats are 1-indexed, so use size 41
        for person, hat_list in enumerate(hats):
            for hat in hat_list:
                hat_to_people[hat].append(person)
        
        # dp[mask] represents the number of ways to assign hats given the current mask
        dp = [0] * (1 << n)
        dp[0] = 1  # Base case: one way to assign 0 hats (do nothing)

        # Iterate over each hat from 1 to 40
        for hat in range(1, 41):
            # Work backwards to avoid overwriting dp states within the same hat
            new_dp = dp[:]  # Create a copy of dp to use for updating states
            for mask in range((1 << n)):
                if dp[mask] == 0:
                    continue
                # Try to assign the current hat to each person who likes this hat
                for person in hat_to_people[hat]:
                    if not (mask & (1 << person)):  # If this person hasn't been assigned a hat
                        new_mask = mask | (1 << person)  # Assign hat to this person
                        new_dp[new_mask] = (new_dp[new_mask] + dp[mask]) % MOD
            dp = new_dp  # Update dp to reflect new states
        
        # The answer is the number of ways to assign hats such that all people have hats
        return dp[(1 << n) - 1]