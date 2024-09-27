class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Convert number to a list of digits
        digits = list(map(int, str(n)))
        length = len(digits)
        
        # Find the first place where the number is not monotone increasing
        mark = length
        for i in range(length - 1):
            if digits[i] > digits[i + 1]:
                mark = i
                break
        
        # If no decrease was found, the number is already monotone increasing
        if mark == length:
            return n
        
        # Decrease the digit at mark and set all following digits to 9
        while mark > 0 and digits[mark] == digits[mark - 1]:
            mark -= 1
        
        digits[mark] -= 1
        for i in range(mark + 1, length):
            digits[i] = 9
        
        # Convert the list of digits back to an integer
        return int(''.join(map(str, digits)))
