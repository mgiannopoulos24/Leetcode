class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Monotonic stack to find the next and previous smaller elements
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                prev_smaller[stack.pop()] = i
            stack.append(i)

        # Calculate the max min-product
        max_product = 0
        for i in range(n):
            left = prev_smaller[i] + 1
            right = next_smaller[i] - 1
            total_sum = prefix[right + 1] - prefix[left]
            max_product = max(max_product, nums[i] * total_sum)

        return max_product % MOD
