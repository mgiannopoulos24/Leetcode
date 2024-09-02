from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse the list of characters s in-place.
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the pointers towards the center
            left += 1
            right -= 1
