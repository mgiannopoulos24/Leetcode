class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        
        # Initialize the magical string with "122"
        s = ['1', '2', '2']
        # Count of '1's in the magical string
        count_ones = 1  # Initial count from the starting "122"
        
        # Pointer to track the number of characters to append
        index = 2
        
        # Generate the magical string until its length is at least n
        while len(s) < n:
            # How many times to append the next character
            append_count = int(s[index])
            
            # Determine the character to append
            char_to_append = '1' if s[-1] == '2' else '2'
            
            # Append the character and count '1's
            for _ in range(append_count):
                if len(s) >= n:
                    break
                s.append(char_to_append)
                if char_to_append == '1':
                    count_ones += 1
            
            # Move to the next index
            index += 1
        
        # Return the count of '1's in the first n characters
        return count_ones
