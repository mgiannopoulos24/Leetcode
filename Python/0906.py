class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        """
        Determines the number of super-palindromes within the inclusive range [left, right].
        
        A super-palindrome is a number that is a palindrome and the square of a palindrome.
        
        :param left: The lower bound of the range as a string.
        :param right: The upper bound of the range as a string.
        :return: The count of super-palindromes within [left, right].
        """
        L = int(left)
        R = int(right)
        count = 0

        # Function to check if a number is a palindrome
        def is_palindrome(x: int) -> bool:
            s = str(x)
            return s == s[::-1]

        # Generate palindromic roots
        # We can limit the first half up to 10^5 to cover roots up to 10^9
        # because the square of 10^5 is 10^10, and we need roots up to 10^9 for squares up to 10^18
        # However, to cover all possible palindromic roots, iterate up to a higher limit if necessary
        # Considering the maximum required root is 10^9, first half up to 10^5 is sufficient

        # Generate palindromes of even length
        for k in range(1, 100000):
            s = str(k)
            rs = s[::-1]
            palindrome = int(s + rs)  # Even length palindrome
            square = palindrome * palindrome
            if square > R:
                break  # No need to continue further
            if square >= L and is_palindrome(square):
                count += 1

        # Generate palindromes of odd length
        for k in range(1, 100000):
            s = str(k)
            rs = s[::-1]
            # Remove the last digit for odd length
            palindrome = int(s + rs[1:])  # Odd length palindrome
            square = palindrome * palindrome
            if square > R:
                break  # No need to continue further
            if square >= L and is_palindrome(square):
                count += 1

        return count
