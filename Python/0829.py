class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        k = 1
        while (k * (k - 1)) // 2 < n:
            # Calculate the sum of the first k-1 integers
            sum_of_first_k_minus_1 = (k * (k - 1)) // 2
            # Check if n - sum_of_first_k_minus_1 is divisible by k
            if (n - sum_of_first_k_minus_1) % k == 0:
                count += 1
            k += 1
        return count
