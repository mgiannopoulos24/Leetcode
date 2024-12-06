class Solution:
    def longestAwesome(self, s: str) -> int:
        # Hash map to store the first occurrence of each bitmask
        seen = {0: -1}  # Initialize with bitmask 0 at index -1 (before the start)
        max_len = 0
        current_mask = 0
        
        for i, char in enumerate(s):
            # Update the current mask by toggling the bit corresponding to the current character
            digit = int(char)
            current_mask ^= (1 << digit)
            
            # Check if we've seen this bitmask before
            if current_mask in seen:
                max_len = max(max_len, i - seen[current_mask])
            else:
                seen[current_mask] = i
            
            # Check for all masks that differ by exactly one bit (allowing one odd-count digit)
            for j in range(10):
                mask_with_one_bit_flipped = current_mask ^ (1 << j)
                if mask_with_one_bit_flipped in seen:
                    max_len = max(max_len, i - seen[mask_with_one_bit_flipped])
        
        return max_len
