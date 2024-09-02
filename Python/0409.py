from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count the frequency of each character
        char_count = Counter(s)
        
        length = 0
        odd_found = False
        
        # Calculate the length of the longest palindrome
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        # If there was at least one odd count, we can add one more to the length
        if odd_found:
            length += 1
        
        return length