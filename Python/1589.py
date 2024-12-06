class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)  # Create a frequency array
        
        # Mark the start and end+1 positions using difference array technique
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1
        
        # Convert the difference array into actual frequency counts
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
        # Remove the extra element from freq
        freq.pop()
        
        # Sort nums and frequency array
        nums.sort()
        freq.sort()
        
        # Calculate the result by summing the products of corresponding values
        MOD = 10**9 + 7
        result = sum(a * b for a, b in zip(nums, freq)) % MOD
        
        return result
