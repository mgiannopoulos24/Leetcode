from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Initialize pointers for reading and writing
        write = 0
        read = 0
        
        while read < len(chars):
            # Start of the current group
            char = chars[read]
            count = 0
            
            # Count the number of consecutive characters
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character and its count (if greater than 1)
            chars[write] = char
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
