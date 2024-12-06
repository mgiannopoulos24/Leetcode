class Solution:
    def minimumDeletions(self, s: str) -> int:
        result = 0  # Minimum deletions required
        count_b = 0  # Number of 'b's encountered so far
        
        for c in s:
            if c == 'a':
                # Option 1: Delete this 'a' (result + 1)
                # Option 2: Delete all previous 'b's (count_b)
                result = min(result + 1, count_b)
            else:
                # Current character is 'b', increment count_b
                count_b += 1
                
        return result
