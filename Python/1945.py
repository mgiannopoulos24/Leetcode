class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert the string s to its numeric representation
        numeric_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Step 2: Compute the digit sum k times
        current_sum = sum(int(char) for char in numeric_str)
        
        # Repeat the transformation k-1 times (since we've done it once already)
        for _ in range(k - 1):
            current_sum = sum(int(char) for char in str(current_sum))
        
        return current_sum