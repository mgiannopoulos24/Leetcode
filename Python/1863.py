class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index: int, current_xor: int) -> int:
            if index == len(nums):
                return current_xor

            # Include the current number in the XOR total
            include = dfs(index + 1, current_xor ^ nums[index])

            # Exclude the current number from the XOR total
            exclude = dfs(index + 1, current_xor)

            return include + exclude

        return dfs(0, 0)
