class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        for i in range(1, n + 1):
            # Find the number of bits required to represent `i`
            length = i.bit_length()
            # Shift result left by 'length' bits and add the current number `i`
            result = ((result << length) | i) % MOD
        return result
