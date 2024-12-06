class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert the number to a list of characters (digits)
        num_str = list(str(num))
        
        # Find the first '6' and change it to '9'
        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break  # Only change the first occurrence
        
        # Convert the list of characters back to an integer and return
        return int(''.join(num_str))
