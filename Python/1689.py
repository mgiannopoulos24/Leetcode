class Solution:
    def minPartitions(self, n: str) -> int:
        # Return the maximum digit in the string as an integer
        return max(int(digit) for digit in n)
