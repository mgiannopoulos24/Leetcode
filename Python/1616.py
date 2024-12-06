class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # Helper function to check if s[l:r+1] is a palindrome
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        # Function to check if a valid palindrome can be formed with a_prefix + b_suffix or b_prefix + a_suffix
        def check(a, b):
            l, r = 0, len(a) - 1
            while l < r and a[l] == b[r]:
                l += 1
                r -= 1
            # Check if the remaining part of a or b forms a palindrome
            return is_palindrome(a, l, r) or is_palindrome(b, l, r)
        
        # Check both possible formations: a_prefix + b_suffix and b_prefix + a_suffix
        return check(a, b) or check(b, a)
