class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x in (2, 3):
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True

        def generate_palindromes():
            # Yield palindromes starting from length 1 upwards
            for length in range(1, 10):  # Only odd lengths up to 9
                for first_half in range(10**(length-1), 10**length):
                    # Create odd-length palindrome by mirroring first_half
                    half_str = str(first_half)
                    palindrome = int(half_str + half_str[-2::-1])  # Mirror except the last character
                    yield palindrome

        # Check small cases directly
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        # Start generating palindromes
        for pal in generate_palindromes():
            if pal >= n and is_prime(pal):
                return pal

        # As we are generating infinite palindromes, the loop will eventually return.
        return -1  # This line is not reachable
