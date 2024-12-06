class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # Step 1: Check if the string is already a palindrome
        if s == s[::-1]:
            return 1
        
        # Step 2: If it's not a palindrome, return 2
        return 2
