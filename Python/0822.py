class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # Step 1: Collect all numbers that are on both the front and back of the same card
        invalid_set = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}
        
        # Step 2: Find the minimum number that is not in the invalid_set
        min_good = float('inf')
        
        # Check all front and back numbers and find the minimum "good" number
        for i in range(len(fronts)):
            if fronts[i] not in invalid_set:
                min_good = min(min_good, fronts[i])
            if backs[i] not in invalid_set:
                min_good = min(min_good, backs[i])
        
        # Step 3: Return the minimum good number or 0 if no good number found
        return min_good if min_good != float('inf') else 0
