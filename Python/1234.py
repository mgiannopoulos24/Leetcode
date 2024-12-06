from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        
        # Step 1: Count the frequencies of the characters in the string
        count = Counter(s)
        
        # Step 2: Check if the string is already balanced
        if all(count[char] <= target for char in "QWER"):
            return 0
        
        # Step 3: Sliding window to find the smallest substring that, if replaced, balances the string
        min_len = n  # Start with the maximum possible length (the whole string)
        left = 0
        
        for right in range(n):
            # Decrease the count of the character as we add it to the window
            count[s[right]] -= 1
            
            # Try to shrink the window from the left as long as the rest of the string can still be balanced
            while all(count[char] <= target for char in "QWER"):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1  # Restore the character at `left` when shrinking the window
                left += 1
        
        return min_len
