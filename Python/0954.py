from collections import Counter
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # Count the frequency of each number
        count = Counter(arr)
        
        # Sort the unique numbers
        unique_nums = sorted(count, key=abs)
        
        for num in unique_nums:
            if count[num] > count[2 * num]:
                return False
            count[2 * num] -= count[num]
        
        return True
