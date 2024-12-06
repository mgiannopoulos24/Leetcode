class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        
        # Convert seat rows to bitmask representation
        seat_mask = []
        for row in seats:
            mask = 0
            for i in range(n):
                if row[i] == '.':
                    mask |= (1 << i)
            seat_mask.append(mask)
        
        # DP array, initially all set to -1 (invalid)
        dp = [[-1] * (1 << n) for _ in range(m)]
        
        # Helper function to count bits set to 1
        def count_bits(x):
            count = 0
            while x:
                count += x & 1
                x >>= 1
            return count
        
        # Check if a bitmask is valid (no students can see each other in the same row)
        def is_valid(mask):
            return (mask & (mask >> 1)) == 0
        
        # Initialize DP for the first row
        for mask in range(1 << n):
            if (mask & seat_mask[0]) == mask and is_valid(mask):
                dp[0][mask] = count_bits(mask)
        
        # Process each row
        for i in range(1, m):
            for prev_mask in range(1 << n):
                if dp[i-1][prev_mask] == -1:
                    continue
                # Try all possible masks for the current row
                for mask in range(1 << n):
                    if (mask & seat_mask[i]) == mask and is_valid(mask):
                        # Check if no student can cheat from previous row
                        if (prev_mask & (mask >> 1)) == 0 and (prev_mask & (mask << 1)) == 0:
                            dp[i][mask] = max(dp[i][mask], dp[i-1][prev_mask] + count_bits(mask))
        
        # Return the maximum students placed in the last row with any valid configuration
        return max(dp[m-1])
