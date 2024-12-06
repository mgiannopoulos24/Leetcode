class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 1  # At least one character is there, so power is at least 1
        current_len = 1
        
        # Iterate through the string starting from the second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_len += 1
            else:
                max_len = max(max_len, current_len)
                current_len = 1  # Reset for the new character
        
        # Final check to handle the last substring
        max_len = max(max_len, current_len)
        
        return max_len
