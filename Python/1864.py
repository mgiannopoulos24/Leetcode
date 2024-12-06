class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        count_0, count_1 = s.count('0'), s.count('1')

        # Check if it's impossible to alternate
        if abs(count_0 - count_1) > 1:
            return -1

        def swaps_needed(pattern: str) -> int:
            swaps = 0
            for i in range(n):
                if s[i] != pattern[i % 2]:
                    swaps += 1
            return swaps // 2

        if count_0 > count_1:
            # Pattern starts with '0'
            pattern = '01' * (n // 2) + ('0' if n % 2 else '')
            return swaps_needed(pattern)
        elif count_1 > count_0:
            # Pattern starts with '1'
            pattern = '10' * (n // 2) + ('1' if n % 2 else '')
            return swaps_needed(pattern)
        else:
            # Both patterns are possible, take the minimum swaps
            pattern1 = '01' * (n // 2) + ('0' if n % 2 else '')
            pattern2 = '10' * (n // 2) + ('1' if n % 2 else '')
            return min(swaps_needed(pattern1), swaps_needed(pattern2))
