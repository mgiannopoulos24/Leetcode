from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1  # Start with the first line
        current_width = 0
        
        for char in s:
            char_width = widths[ord(char) - ord('a')]  # Get the width of the character
            if current_width + char_width > 100:
                # If adding this character exceeds 100 pixels, start a new line
                lines += 1
                current_width = char_width  # This character starts the new line
            else:
                current_width += char_width  # Add to the current line's width
        
        return [lines, current_width]
