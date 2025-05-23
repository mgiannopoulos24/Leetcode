class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        
        # Two patterns to compare against
        # pattern1 starts with '0', pattern2 starts with '1'
        mismatch1 = 0  # mismatches for pattern starting with '0'
        mismatch2 = 0  # mismatches for pattern starting with '1'
        res = float('inf')

        for i in range(n):
            # For even position (0-based), expected chars are:
            expected1 = '0' if i % 2 == 0 else '1'
            expected2 = '1' if i % 2 == 0 else '0'

            if s[i] != expected1:
                mismatch1 += 1
            if s[i] != expected2:
                mismatch2 += 1

        # Store initial min flips
        res = min(mismatch1, mismatch2)

        # Sliding window to simulate rotation
        # For strings of even length, only n rotations matter
        # For strings of odd length, we have to simulate up to 2n
        for i in range(n):
            # Remove the first character and add it to end
            # Update mismatches for both patterns
            front_char = s[i]
            
            # For pattern1
            if i % 2 == 0:
                if front_char != '0': mismatch1 -= 1
            else:
                if front_char != '1': mismatch1 -= 1
            
            # Add new character at the end (same as front_char)
            if (i + n) % 2 == 0:
                if front_char != '0': mismatch1 += 1
            else:
                if front_char != '1': mismatch1 += 1
            
            # For pattern2
            if i % 2 == 0:
                if front_char != '1': mismatch2 -= 1
            else:
                if front_char != '0': mismatch2 -= 1
            
            if (i + n) % 2 == 0:
                if front_char != '1': mismatch2 += 1
            else:
                if front_char != '0': mismatch2 += 1

            res = min(res, mismatch1, mismatch2)

        return res