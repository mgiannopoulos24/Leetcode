class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a' * n  # For odd n, return n occurrences of 'a'
        else:
            return 'a' * (n - 1) + 'b'  # For even n, return (n-1) 'a's and 1 'b'
