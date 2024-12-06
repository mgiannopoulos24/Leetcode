class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)

        # Frequency array to store counts of each number in nums
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1

        # Prefix sum to calculate cumulative frequencies
        prefix = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix[i] = prefix[i - 1] + freq[i]

        result = 0
        for num in range(1, max_num + 1):
            if freq[num] > 0:
                # Calculate contributions for multiples of num
                for multiple in range(num, max_num + 1, num):
                    left = multiple
                    right = min(max_num, multiple + num - 1)
                    count = prefix[right] - prefix[left - 1]
                    result += freq[num] * count * (multiple // num)
                    result %= MOD

        return result
