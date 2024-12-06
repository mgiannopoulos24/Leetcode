class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Step 1: Sort the positions
        position.sort()
        
        # Step 2: Binary search on the answer (min force)
        def canPlaceBalls(d):
            # Try to place the first ball at the first position
            count = 1
            last_pos = position[0]
            
            # Try to place the remaining balls
            for i in range(1, len(position)):
                if position[i] - last_pos >= d:
                    count += 1
                    last_pos = position[i]
                if count == m:
                    return True
            return False
        
        # Binary search for the maximum minimum distance
        left, right = 1, position[-1] - position[0]
        best_dist = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                best_dist = mid  # mid is a valid distance, so we try for a larger one
                left = mid + 1
            else:
                right = mid - 1
        
        return best_dist
