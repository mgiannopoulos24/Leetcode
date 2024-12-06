class Solution:
    def minOperations(self, n: int) -> int:
        # We are summing the difference between each element in the first half of the array and n
        return (n // 2) * (n - n // 2)
