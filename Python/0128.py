from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)  # Create a set of the numbers
        longest_streak = 0
        
        for num in num_set:
            # Check if this number is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Expand the sequence as long as consecutive numbers are present
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak found
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
