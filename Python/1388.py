class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def max_slices(arr, n):
            length = len(arr)
            # dp[i][j]: max sum we can get by selecting j slices from the first i slices
            dp = [[0] * (n + 1) for _ in range(length + 1)]
            
            for i in range(1, length + 1):
                for j in range(1, n + 1):
                    # Transition state
                    dp[i][j] = max(dp[i-1][j], (dp[i-2][j-1] + arr[i-1]) if i > 1 else arr[i-1])
                    
            return dp[length][n]
        
        n = len(slices) // 3
        # Case 1: Ignore the first slice (slices[1:])
        case1 = max_slices(slices[1:], n)
        # Case 2: Ignore the last slice (slices[:-1])
        case2 = max_slices(slices[:-1], n)
        
        return max(case1, case2)
