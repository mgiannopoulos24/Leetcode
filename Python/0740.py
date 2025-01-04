from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Count the occurrences of each number
        count = defaultdict(int)
        for num in nums:
            count[num] += num
        
        # Find the maximum number in nums
        max_num = max(count.keys())
        
        # Initialize dp array
        dp = [0] * (max_num + 1)
        dp[1] = count.get(1, 0)
        
        # Fill the dp array
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + count.get(i, 0))
        
        return dp[max_num]