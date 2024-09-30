from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Step 1: Sort the array of people by weight
        people.sort()
        
        # Step 2: Initialize two pointers
        left = 0
        right = len(people) - 1
        boats = 0
        
        # Step 3: Use two pointers to find the minimum number of boats needed
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # Person at 'left' is paired with 'right'
            right -= 1  # Person at 'right' is placed in a boat
            boats += 1  # One more boat is used
        
        return boats
