class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # Helper function to perform Rabin-Karp for a given length `L`
        def search(L: int, modulus: int) -> int:
            """Search for a duplicate substring of length L using rolling hash."""
            h = 0
            # Base value for the rolling hash function
            a = 26
            # Compute the hash of the first window of size L
            for i in range(L):
                h = (h * a + nums[i]) % modulus

            # Store the hash of the first window
            seen = {h}
            # a^L % modulus
            aL = pow(a, L, modulus)

            # Rolling hash over the string
            for start in range(1, n - L + 1):
                # Compute the rolling hash in O(1) time
                h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
                if h in seen:
                    return start
                seen.add(h)
            return -1

        # Transform the string `s` into array of integers `nums`
        # 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        # Binary search parameters
        left, right = 1, n
        longest_dup = ""
        modulus = 2**63 - 1  # A large prime number

        while left < right:
            mid = (left + right) // 2
            start = search(mid, modulus)
            if start != -1:  # Duplicate substring of length `mid` found
                longest_dup = s[start:start + mid]
                left = mid + 1  # Try for a longer length
            else:
                right = mid  # Try for a shorter length
        
        return longest_dup
