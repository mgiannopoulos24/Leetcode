class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # Count the number of '0's in the string
        count_zeros = binary.count('0')
        
        # If there are fewer than 2 zeros, no transformation is possible or necessary
        if count_zeros <= 1:
            return binary
        
        # Find the first occurrence of '0'
        first_zero_index = binary.index('0')
        
        # Build the result string:
        # 1. Leading '1's that were unaffected (everything before the first '0').
        # 2. After pushing all zeros to the right, there will be one '0' at position (first_zero_index + count_zeros - 1).
        # 3. All other positions are filled with '1's.
        
        # All leading '1's remain intact, then we have count_zeros - 1 '1's followed by one '0'
        # and the rest are '1's.
        result = '1' * first_zero_index + '1' * (count_zeros - 1) + '0' + '1' * (len(binary) - first_zero_index - count_zeros)
        
        return result
