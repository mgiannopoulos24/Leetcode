from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        # Step 1: Find the minimum and maximum values
        min_val, max_val = min(nums), max(nums)
        
        # Step 2: Calculate the bucket size and number of buckets
        bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Step 3: Initialize buckets
        buckets = [[None, None] for _ in range(bucket_count)]
        
        # Step 4: Place each number in the appropriate bucket
        for num in nums:
            idx = (num - min_val) // bucket_size
            if buckets[idx][0] is None:
                buckets[idx][0] = num
                buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
        
        # Step 5: Calculate the maximum gap
        max_gap = 0
        prev_max = None
        
        for bucket in buckets:
            if bucket[0] is not None:
                if prev_max is not None:
                    max_gap = max(max_gap, bucket[0] - prev_max)
                prev_max = bucket[1]
        
        return max_gap
