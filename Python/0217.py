from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create an empty set to keep track of seen elements
        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)  # Add the element to the set
        return False  # No duplicates found
