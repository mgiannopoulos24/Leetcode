class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle negative numbers
        if x < 0:
            return False
        
        # Convert integer to string
        s = str(x)
        
        # Initialize pointers
        left, right = 0, len(s) - 1
        
        # Check palindrome condition
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
