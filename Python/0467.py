class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # Array to store the maximum length of wraparound substrings ending with each character
        max_len = [0] * 26
        current_len = 0
        
        for i in range(len(s)):
            # Calculate index of the current character
            index = ord(s[i]) - ord('a')
            
            # Check if the current character is a continuation of the wraparound sequence
            if i > 0 and (ord(s[i]) == ord(s[i - 1]) + 1 or (s[i - 1] == 'z' and s[i] == 'a')):
                current_len += 1
            else:
                current_len = 1
            
            # Update the maximum length for the current character
            max_len[index] = max(max_len[index], current_len)
        
        # Calculate the total number of unique substrings
        result = sum(max_len)
        
        return result
