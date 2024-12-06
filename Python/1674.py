class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)  # Difference array to track changes in the number of moves

        # For each pair (nums[i], nums[n-1-i]), calculate the impact on moves
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            low = 1 + min(a, b)  # Minimum sum after one move
            high = limit + max(a, b)  # Maximum sum after one move
            target_sum = a + b  # The sum without any move

            # We need 2 moves outside of [low, high]
            delta[2] += 2  # 2 moves needed for sum 2 or less
            delta[low] -= 1  # 1 move needed from sum `low`
            delta[target_sum] -= 1  # No move needed at `target_sum`
            delta[target_sum + 1] += 1  # 1 move needed after `target_sum`
            delta[high + 1] += 1  # 2 moves needed after `high`

        # Calculate the minimum moves by processing the difference array
        moves = 0
        min_moves = float('inf')
        for i in range(2, 2 * limit + 1):
            moves += delta[i]
            min_moves = min(min_moves, moves)
        
        return min_moves
