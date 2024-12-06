from collections import defaultdict

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = defaultdict(int)  # Frequency of each number
        freqCount = defaultdict(int)  # How many numbers have a certain frequency
        maxLen = 0
        n = len(nums)
        
        for i in range(n):
            num = nums[i]
            
            # If num already has a frequency, decrease the freqCount for that frequency
            if freq[num] > 0:
                freqCount[freq[num]] -= 1
                if freqCount[freq[num]] == 0:
                    del freqCount[freq[num]]
            
            # Increase the frequency of num
            freq[num] += 1
            
            # Increase the freqCount for the new frequency
            freqCount[freq[num]] += 1
            
            # The total number of unique frequencies
            uniqueFreqs = list(freqCount.keys())
            
            # Case 1: All numbers appear the same number of times (1 unique frequency)
            if len(freqCount) == 1:
                freqValue = uniqueFreqs[0]
                if freqValue == 1 or freqCount[freqValue] == 1:
                    maxLen = i + 1
            
            # Case 2: Two unique frequencies, with specific conditions
            if len(freqCount) == 2:
                freq1, freq2 = sorted(uniqueFreqs)
                
                # Check if removing one element makes all frequencies equal
                # Scenario 1: freq1 = 1 and freqCount[freq1] == 1 (meaning one element appears only once)
                if freq1 == 1 and freqCount[freq1] == 1:
                    maxLen = i + 1
                
                # Scenario 2: freq2 = freq1 + 1 and freqCount[freq2] == 1 (meaning one element appears one more time than others)
                elif freq2 == freq1 + 1 and freqCount[freq2] == 1:
                    maxLen = i + 1

        return maxLen
