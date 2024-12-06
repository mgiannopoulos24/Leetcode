from functools import lru_cache
from itertools import combinations

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k
        
        # Check if it's possible to create valid subsets without duplicates
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > k:
                return -1  # Impossible because some element appears more than `k` times
        
        # Precompute valid subsets of size `subset_size` that contain no duplicates
        all_subsets = []
        for subset in combinations(range(n), subset_size):
            subset_values = [nums[i] for i in subset]
            if len(set(subset_values)) == subset_size:  # Ensure no duplicates
                incompatibility = max(subset_values) - min(subset_values)
                mask = sum(1 << i for i in subset)  # Bitmask representation
                all_subsets.append((mask, incompatibility))
        
        # Use memoization to store results of intermediate states
        @lru_cache(None)
        def dp(mask, groups_left):
            if groups_left == 0:
                return 0 if mask == 0 else float('inf')
            
            result = float('inf')
            for subset_mask, inc in all_subsets:
                if mask & subset_mask == subset_mask:  # If subset_mask is fully included in mask
                    result = min(result, inc + dp(mask ^ subset_mask, groups_left - 1))
            return result
        
        # Start with all elements available (mask with all bits set to 1)
        full_mask = (1 << n) - 1
        return dp(full_mask, k)
