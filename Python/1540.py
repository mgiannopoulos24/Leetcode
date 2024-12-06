class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        # If s and t have different lengths, it's impossible to convert
        if len(s) != len(t):
            return False
        
        # Array to track how many times a particular shift difference is needed
        shift_counts = [0] * 26
        
        # Traverse both strings and calculate the shift differences
        for i in range(len(s)):
            # Calculate the shift difference between s[i] and t[i]
            shift_diff = (ord(t[i]) - ord(s[i]) + 26) % 26
            if shift_diff > 0:
                shift_counts[shift_diff] += 1
        
        # Now check if it's possible to perform all necessary shifts within k moves
        for d in range(1, 26):  # Shift difference 0 doesn't need any moves
            max_moves_needed = (shift_counts[d] - 1) * 26 + d
            if max_moves_needed > k:
                return False
        
        return True
