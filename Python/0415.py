class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Reverse both strings to facilitate addition from least significant digit
        num1, num2 = num1[::-1], num2[::-1]
        
        carry = 0
        result = []
        
        # Process both strings
        max_length = max(len(num1), len(num2))
        
        for i in range(max_length):
            # Get the current digit from num1 and num2, default to 0 if index is out of range
            digit1 = int(num1[i]) if i < len(num1) else 0
            digit2 = int(num2[i]) if i < len(num2) else 0
            
            # Add digits and carry
            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(total % 10)
        
        # If there's a carry left after the final addition, add it to the result
        if carry:
            result.append(carry)
        
        # The result list is in reverse order, so reverse it back and convert to string
        return ''.join(map(str, result[::-1]))
