from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Step 1: Count the frequency of each element in the array
        freq = Counter(arr)
        
        # Step 2: Initialize the result as -1 (default if no lucky number is found)
        largest_lucky = -1
        
        # Step 3: Iterate through the frequency map and check for lucky numbers
        for num, count in freq.items():
            if num == count:
                largest_lucky = max(largest_lucky, num)
        
        return largest_lucky
