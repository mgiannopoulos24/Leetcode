class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function to check if a string is a palindrome
        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try skipping the left character or the right character
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
            left += 1
            right -= 1
        
        # If no mismatches found, it's already a palindrome
        return True
