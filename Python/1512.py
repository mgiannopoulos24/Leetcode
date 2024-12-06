class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq = {}

        # Iterate through each number in the array
        for num in nums:
            if num in freq:
                # If num has already been seen, the number of good pairs
                # increases by the frequency of the current num
                count += freq[num]
                freq[num] += 1
            else:
                # If num is seen for the first time, initialize its frequency
                freq[num] = 1

        return count
