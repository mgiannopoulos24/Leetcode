class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        total_count = 0
        count = 1  # Initialize count for the first character
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1  # Increment the count of consecutive identical characters
            else:
                # Add homogenous substrings count for the previous sequence
                total_count += count * (count + 1) // 2
                total_count %= MOD  # Take modulo to avoid overflow
                count = 1  # Reset count for the new character
        
        # Add the homogenous substrings count for the last sequence
        total_count += count * (count + 1) // 2
        total_count %= MOD  # Final modulo adjustment
        
        return total_count
