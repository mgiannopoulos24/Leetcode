class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # Dictionary to store the maximum height of the taller support for each difference
        dp = {0: 0}
        
        for rod in rods:
            # New dictionary to store updated states
            new_dp = dp.copy()
            
            for diff, height in dp.items():
                # Add rod to the taller support, increasing the height difference
                new_dp[diff + rod] = max(new_dp.get(diff + rod, 0), height)
                
                # Add rod to the shorter support, reducing the height difference
                new_dp[abs(diff - rod)] = max(new_dp.get(abs(diff - rod), 0), height + min(diff, rod))
            
            dp = new_dp
        
        return dp[0]
