class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n  # dp[i] will store the maximum jumps starting from index i

        # Function to compute the maximum jumps starting from index i
        def dfs(i):
            if dp[i] != -1:
                return dp[i]  # Return the cached result if already computed

            max_jump = 1  # Start by considering the current index only

            # Jump to the right
            for x in range(1, d + 1):
                if i + x < n and arr[i] > arr[i + x]:
                    max_jump = max(max_jump, 1 + dfs(i + x))
                else:
                    break  # Stop if the jump is not valid (no further jumps possible)

            # Jump to the left
            for x in range(1, d + 1):
                if i - x >= 0 and arr[i] > arr[i - x]:
                    max_jump = max(max_jump, 1 + dfs(i - x))
                else:
                    break  # Stop if the jump is not valid (no further jumps possible)

            dp[i] = max_jump  # Cache the result
            return dp[i]

        # Compute the maximum jumps for each index and return the global maximum
        return max(dfs(i) for i in range(n))
