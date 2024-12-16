from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Variables to track the maximum values for each of the positions in the triplets
        max_a, max_b, max_c = 0, 0, 0
        
        # Iterate through each triplet
        for triplet in triplets:
            a, b, c = triplet
            # If any element in the triplet exceeds the target, we can't form the target
            if a > target[0] or b > target[1] or c > target[2]:
                continue  # This triplet is not useful
            
            # Update the max values we can achieve
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            max_c = max(max_c, c)
        
        # After processing all triplets, check if we can achieve the target
        return [max_a, max_b, max_c] == target
