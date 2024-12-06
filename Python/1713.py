from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # Map each element in target to its index
        pos_map = {val: i for i, val in enumerate(target)}
        
        # Filter arr to contain only indices in pos_map, in order
        filtered = [pos_map[val] for val in arr if val in pos_map]
        
        # Find the LIS of filtered array
        lis = []
        for x in filtered:
            idx = bisect_left(lis, x)
            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x
        
        # The minimum number of operations
        return len(target) - len(lis)
