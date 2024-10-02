from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # Set to store distinct bitwise OR results
        distinct_ors = set()
        # Set to keep track of OR values ending at the current index
        current_or = set()
        
        for num in arr:
            # New OR values including the current number
            new_or = {num}
            for val in current_or:
                new_or.add(val | num)
            
            # Update the global set of distinct ORs
            distinct_ors.update(new_or)
            
            # Update the current OR values for the next index
            current_or = new_or
        
        return len(distinct_ors)
