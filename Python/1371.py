class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Map vowels to specific bit positions
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        # Dictionary to store the first occurrence of each bitmask
        # Initialize with 0 -> -1 to handle the case where the entire substring is valid
        seen = {0: -1}
        
        bitmask = 0  # To track the bitmask of vowels
        max_len = 0  # To store the maximum length of the valid substring
        
        # Iterate over the string
        for i, char in enumerate(s):
            if char in vowels:
                # Flip the corresponding bit for the vowel
                bitmask ^= (1 << vowels[char])
            
            # If the current bitmask has been seen before, calculate the length of the valid substring
            if bitmask in seen:
                max_len = max(max_len, i - seen[bitmask])
            else:
                # Otherwise, store the first occurrence of this bitmask
                seen[bitmask] = i
        
        return max_len
