class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            # Character to be removed from both ends
            char = s[left]
            
            # Move left pointer to the right past all identical chars
            while left <= right and s[left] == char:
                left += 1
                
            # Move right pointer to the left past all identical chars
            while left <= right and s[right] == char:
                right -= 1
        
        # Return the remaining length
        return right - left + 1
