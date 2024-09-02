from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # Helper function to check if a byte is a valid continuation byte
        def is_continuation_byte(byte):
            return (byte & 0b11000000) == 0b10000000
        
        # Number of continuation bytes expected
        num_bytes = 0
        
        for byte in data:
            # Check how many leading 1's are in the byte
            if num_bytes == 0:
                if (byte & 0b10000000) == 0b00000000:
                    # 1-byte character
                    continue
                elif (byte & 0b11100000) == 0b11000000:
                    # 2-byte character
                    num_bytes = 1
                elif (byte & 0b11110000) == 0b11100000:
                    # 3-byte character
                    num_bytes = 2
                elif (byte & 0b11111000) == 0b11110000:
                    # 4-byte character
                    num_bytes = 3
                else:
                    # Invalid starting byte
                    return False
            else:
                # We are in a continuation byte
                if not is_continuation_byte(byte):
                    return False
                num_bytes -= 1
        
        # Ensure we do not expect any more continuation bytes
        return num_bytes == 0
