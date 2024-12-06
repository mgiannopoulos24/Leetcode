class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        pattern1_mismatch = 0  # Mismatches for "010101..."
        pattern2_mismatch = 0  # Mismatches for "101010..."
        
        for i in range(n):
            expected_char_pattern1 = '0' if i % 2 == 0 else '1'
            expected_char_pattern2 = '1' if i % 2 == 0 else '0'
            
            # Count mismatches for pattern starting with '0' (pattern1)
            if s[i] != expected_char_pattern1:
                pattern1_mismatch += 1
            
            # Count mismatches for pattern starting with '1' (pattern2)
            if s[i] != expected_char_pattern2:
                pattern2_mismatch += 1
        
        # Return the minimum mismatches between the two patterns
        return min(pattern1_mismatch, pattern2_mismatch)
