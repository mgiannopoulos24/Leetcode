from typing import List

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        start = 0  # Pointer to track the current start position in nums
        
        # Process each group in sequence
        for group in groups:
            found = False  # Flag to check if the current group is found
            
            # Try to find the group in nums starting from the current start index
            while start + len(group) <= len(nums):
                # Check if the subarray of nums starting at 'start' matches 'group'
                if nums[start:start + len(group)] == group:
                    # If matched, move the start pointer past this group and mark found
                    start += len(group)
                    found = True
                    break
                start += 1  # Move start one step forward if no match
        
            # If the group was not found, return False
            if not found:
                return False
        
        # All groups matched in sequence
        return True
