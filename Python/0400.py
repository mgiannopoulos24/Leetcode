class Solution:
    def findNthDigit(self, n: int) -> int:
        # Step 1: Find the length of the number containing the nth digit
        digit_length = 1
        count = 9
        start = 1
        
        # Determine which length contains the nth digit
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
        
        # Step 2: Find the exact number
        start += (n - 1) // digit_length
        num_str = str(start)
        
        # Step 3: Find the specific digit
        index = (n - 1) % digit_length
        return int(num_str[index])
