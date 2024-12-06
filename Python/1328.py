class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        
        # Base case: If the length is 1, we cannot make it non-palindromic
        if n == 1:
            return ""
        
        # Convert the string to a list of characters to modify it easily
        palindrome = list(palindrome)
        
        # Try to replace the first non-'a' character in the first half of the palindrome
        for i in range(n // 2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
        
        # If no non-'a' character was found, change the last character to 'b'
        palindrome[-1] = 'b'
        return ''.join(palindrome)
