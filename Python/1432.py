class Solution:
    def maxDiff(self, num: int) -> int:
        # Convert the number to a string to process digit by digit
        s = str(num)
        
        # Step 1: Maximize 'a' by replacing the first non-9 digit with '9'
        # Example: 555 -> 999
        # Convert num to a list of characters to manipulate digits
        for digit in s:
            if digit != '9':  # Find the first non-9 digit
                max_a = s.replace(digit, '9')
                break
        else:
            max_a = s  # If all digits are '9', no change
        
        # Step 2: Minimize 'b'
        # If the first digit is not '1', change the first digit to '1'
        if s[0] != '1':
            min_b = s.replace(s[0], '1')
        else:
            # If the first digit is '1', find the first non-1 digit to change it to '0'
            for digit in s[1:]:  # Skip the first digit
                if digit != '1' and digit != '0':  # We can't replace with 0 if it would make a leading 0
                    min_b = s.replace(digit, '0')
                    break
            else:
                min_b = s  # If all digits are '1' or '0', no change
                
        # Convert the modified strings back to integers and compute the difference
        return int(max_a) - int(min_b)