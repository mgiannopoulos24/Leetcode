class Solution:
    def decodeString(self, s: str) -> str:
        char_stack = []
        num_stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the current number (handling multiple digits)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current string and current number to their respective stacks
                num_stack.append(current_num)
                char_stack.append(current_string)
                # Reset current string and current number for the new substring
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop from the stacks to get the previous string and multiplier
                prev_string = char_stack.pop()
                num = num_stack.pop()
                # Repeat the current string num times and append it to the previous string
                current_string = prev_string + current_string * num
            else:
                # Append the current character to the current string
                current_string += char
        
        return current_string
