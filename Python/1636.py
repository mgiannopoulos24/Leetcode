from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count the frequency of each number
        freq = Counter(nums)
        
        # Step 2: Sort the array based on the frequency and then by the value
        # - Sort by frequency (ascending) with `freq[x]`
        # - If frequencies are the same, sort by value (descending) with `-x`
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums
