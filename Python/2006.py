class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        freq = {}

        for num in nums:
            # Check for pairs where the absolute difference is k
            count += freq.get(num - k, 0) + freq.get(num + k, 0)
            
            # Update the frequency of the current number
            freq[num] = freq.get(num, 0) + 1

        return count
