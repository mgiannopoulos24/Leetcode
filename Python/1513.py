class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        length_of_ones = 0

        for char in s:
            if char == '1':
                # Increase the current streak of 1's
                length_of_ones += 1
                count += length_of_ones
            else:
                # Reset streak if we hit a '0'
                length_of_ones = 0
        
        return count % MOD
