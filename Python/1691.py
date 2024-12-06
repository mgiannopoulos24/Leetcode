class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Step 1: Sort each cuboid's dimensions
        for cuboid in cuboids:
            cuboid.sort()

        # Step 2: Sort the cuboids based on dimensions (width, length, height)
        cuboids.sort()

        # Step 3: Initialize DP array
        n = len(cuboids)
        dp = [0] * n
        
        # Step 4: Fill DP array
        for i in range(n):
            dp[i] = cuboids[i][2]  # The height of cuboid[i] in its sorted form
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0] and
                    cuboids[j][1] <= cuboids[i][1] and
                    cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])

        # Step 5: Return the maximum height from the dp array
        return max(dp)
