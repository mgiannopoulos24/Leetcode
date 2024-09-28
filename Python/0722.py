class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        result = []
        current_line = []
        
        for line in source:
            i = 0
            while i < len(line):
                if not in_block:
                    # Look for the start of a block comment or line comment
                    if i + 1 < len(line) and line[i:i+2] == "/*":
                        in_block = True
                        i += 1  # Skip the start of the block comment
                    elif i + 1 < len(line) and line[i:i+2] == "//":
                        break  # Ignore the rest of the line for line comment
                    else:
                        current_line.append(line[i])  # Append valid code character
                else:
                    # Inside a block comment, look for the end of the block comment
                    if i + 1 < len(line) and line[i:i+2] == "*/":
                        in_block = False
                        i += 1  # Skip the end of the block comment
                i += 1
            
            # If we are not in a block comment and current_line has content, append it to result
            if not in_block and current_line:
                result.append("".join(current_line))
                current_line = []
        
        return result
