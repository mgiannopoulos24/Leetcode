class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import defaultdict

        # Dictionaries to store the frequency, first occurrence, and last occurrence
        frequency = defaultdict(int)
        first_occurrence = {}
        last_occurrence = {}
        
        # Traverse the array to populate the dictionaries
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i
            frequency[num] += 1
        
        # Find the degree of the array
        degree = max(frequency.values())
        
        # Find the minimum length of subarray that has the same degree
        min_length = float('inf')
        for num, freq in frequency.items():
            if freq == degree:
                min_length = min(min_length, last_occurrence[num] - first_occurrence[num] + 1)
        
        return min_length
