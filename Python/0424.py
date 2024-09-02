class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        
        left = 0
        max_length = 0
        max_freq = 0
        count = defaultdict(int)
        
        for right in range(len(s)):
            # Include the current character in the window
            count[s[right]] += 1
            
            # Update the maximum frequency of any character in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # Number of characters to replace in the current window
            current_window_size = right - left + 1
            replacements_needed = current_window_size - max_freq
            
            # If replacements exceed k, shrink the window from the left
            if replacements_needed > k:
                count[s[left]] -= 1
                left += 1
            
            # Update the maximum length of a valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length