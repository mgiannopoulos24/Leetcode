from collections import Counter

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        freq = Counter(nums)
        
        for num in nums:
            if target.startswith(num):
                suffix = target[len(num):]
                if suffix in freq:
                    if num == suffix:
                        # If the prefix and suffix are the same, we need to subtract one
                        # to avoid counting the same index twice.
                        count += freq[suffix] - 1
                    else:
                        count += freq[suffix]
        
        return count