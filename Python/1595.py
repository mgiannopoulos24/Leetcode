from functools import lru_cache

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0])
        
        # Memoization
        @lru_cache(None)
        def dp(i, mask):
            if i == size1:  # All points in the first group are processed
                result = 0
                # Add the cost of connecting the remaining points in the second group
                for j in range(size2):
                    if not (mask & (1 << j)):
                        # If point j in the second group is not connected, connect it with the minimum cost
                        result += min(cost[x][j] for x in range(size1))
                return result
            
            result = float('inf')
            for j in range(size2):
                # Try to connect point i from the first group to point j in the second group
                result = min(result, cost[i][j] + dp(i + 1, mask | (1 << j)))
            
            return result
        
        # Call dp starting from 0th point in the first group and no points in the second group connected
        return dp(0, 0)
