from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Step 1: Count the frequency of each number
        count = Counter(nums)
        
        # Step 2: Initialize the maximum length
        max_length = 0
        
        # Step 3: Iterate through each unique number in the count
        for num in count:
            if num + 1 in count:
                # Calculate the length of harmonious subsequence
                length = count[num] + count[num + 1]
                # Update the maximum length
                max_length = max(max_length, length)
        
        return max_length
