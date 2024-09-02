class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Create a frequency dictionary
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Step 2: Find the first unique character
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        # If no unique character is found
        return -1
