class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        positions = [i for i, num in enumerate(nums) if num == 1]
        n = len(positions)
        prefix_sums = [0] * (n + 1)
        adjusted_positions = [0] * n

        # Adjust positions
        for i in range(n):
            adjusted_positions[i] = positions[i] - i
            prefix_sums[i + 1] = prefix_sums[i] + adjusted_positions[i]

        min_cost = float('inf')
        for i in range(n - k + 1):
            l = i
            r = i + k - 1
            m = (l + r) // 2
            median = adjusted_positions[m]

            # Left cost
            left_count = m - l
            left_sum = prefix_sums[m] - prefix_sums[l]
            left_cost = median * left_count - left_sum

            # Right cost
            right_count = r - m
            right_sum = prefix_sums[r + 1] - prefix_sums[m + 1]
            right_cost = right_sum - median * right_count

            total_cost = left_cost + right_cost
            min_cost = min(min_cost, total_cost)

        return int(min_cost)
