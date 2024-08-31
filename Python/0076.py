from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Frequency count of characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Initialize pointers and variables
        l, r = 0, 0
        formed = 0
        window_counts = defaultdict(int)
        min_len = float('inf')
        min_window = ""
        
        # Start sliding the window
        while r < len(s):
            # Add character from the right
            character = s[r]
            window_counts[character] += 1
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # Try and contract the window until it ceases to be 'desirable'
            while l <= r and formed == required:
                character = s[l]
                
                # Update the result if this window is smaller than the previous one
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r + 1]
                
                # The character at the left pointer is no longer a part of the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                l += 1
            
            # Move the right pointer
            r += 1
        
        return min_window