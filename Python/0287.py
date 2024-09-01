from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point in the cycle
        tortoise = nums[0]
        hare = nums[0]
        
        # Move tortoise by 1 step and hare by 2 steps until they meet
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Phase 2: Find the entrance to the cycle
        # Move hare to the start of the array
        hare = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        # The meeting point is the duplicate number
        return hare
