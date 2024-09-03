class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        base7_digits = []
        
        while num > 0:
            remainder = num % 7
            base7_digits.append(str(remainder))
            num //= 7
        
        # Reverse the digits since they are in the reverse order
        base7_string = ''.join(reversed(base7_digits))
        
        return "-" + base7_string if negative else base7_string
