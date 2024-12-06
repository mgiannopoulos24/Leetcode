class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        # Iterate through the list in steps of 2 to get freq and val pairs
        for i in range(0, len(nums), 2):
            freq = nums[i]    # Get the frequency
            val = nums[i + 1] # Get the value
            result.extend([val] * freq)  # Append freq copies of val to the result list
        return result
