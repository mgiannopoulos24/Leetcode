class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Dictionary to store the frequency of bitmasks encountered
        freq_map = {0: 1}  # We start with an empty prefix bitmask with count 1
        current_mask = 0
        result = 0
        
        for ch in word:
            # Update the current bitmask by flipping the corresponding bit for the character
            current_mask ^= (1 << (ord(ch) - ord('a')))
            
            # Add substrings that have the same bitmask as the current one
            if current_mask in freq_map:
                result += freq_map[current_mask]
            
            # Add substrings that differ by exactly one bit
            for i in range(10):
                # Flip each bit one by one and check if the resulting bitmask is in the map
                toggled_mask = current_mask ^ (1 << i)
                if toggled_mask in freq_map:
                    result += freq_map[toggled_mask]
            
            # Update the frequency of the current bitmask
            if current_mask in freq_map:
                freq_map[current_mask] += 1
            else:
                freq_map[current_mask] = 1
        
        return result
