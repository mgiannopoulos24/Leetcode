from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        if len_s1 > len_s2:
            return False
        
        # Frequency count for s1
        s1_count = Counter(s1)
        # Frequency count for the current window in s2
        window_count = Counter()
        
        # Initialize the window count for the first window
        for i in range(len_s1):
            window_count[s2[i]] += 1
        
        # Check the first window
        if window_count == s1_count:
            return True
        
        # Slide the window over s2
        for i in range(len_s1, len_s2):
            # Add the new character to the window
            window_count[s2[i]] += 1
            # Remove the character that is no longer in the window
            window_count[s2[i - len_s1]] -= 1
            
            # If the count becomes zero, remove the character from the count
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]
            
            # Check if the current window matches s1_count
            if window_count == s1_count:
                return True
        
        return False
