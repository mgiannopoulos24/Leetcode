class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Step 1: Check if it's impossible to make m bouquets
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        # Step 2: Define a helper function to check if we can make m bouquets in given 'days'
        def canMakeBouquets(days: int) -> bool:
            bouquets = 0
            flowers = 0  # count of consecutive bloomed flowers
            
            for day in bloomDay:
                if day <= days:
                    flowers += 1
                    # Once we have k consecutive flowers, we can make a bouquet
                    if flowers == k:
                        bouquets += 1
                        flowers = 0  # reset the count for the next bouquet
                else:
                    flowers = 0  # reset if a flower has not bloomed
                
                # If we already have enough bouquets, return True early
                if bouquets >= m:
                    return True
            return False
        
        # Step 3: Binary search for the minimum number of days
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid  # Try for fewer days
            else:
                left = mid + 1  # Increase the number of days
        
        # Step 4: After binary search, check if left is the valid number of days
        return left if canMakeBouquets(left) else -1
