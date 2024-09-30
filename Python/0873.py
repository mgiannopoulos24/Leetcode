from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Dictionary to store index of each value in arr
        index_map = {num: idx for idx, num in enumerate(arr)}
        
        # dp[j][i] will store the length of the longest Fibonacci-like subsequence ending with arr[i] and arr[j]
        dp = {}
        max_length = 0
        
        # Iterate over pairs (i, j)
        for j in range(1, len(arr)):
            for i in range(j):
                # arr[i] and arr[j] are two consecutive elements in a Fibonacci-like sequence
                # Find the previous element in the Fibonacci-like sequence
                k = index_map.get(arr[j] - arr[i], None)
                if k is not None and k < i:
                    # If there is a valid k, update dp[j][i]
                    dp[i, j] = dp.get((k, i), 2) + 1
                else:
                    # If there is no valid k, start a new sequence of length 2
                    dp[i, j] = 2
                # Update the maximum length found so far
                max_length = max(max_length, dp[i, j])
        
        return max_length if max_length >= 3 else 0
