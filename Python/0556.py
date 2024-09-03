class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        
        # Step 1: Find the pivot
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        if i == -1:
            return -1
        
        # Step 2: Find the smallest digit on the right of the pivot which is larger than digits[i]
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        # Step 3: Swap the pivot with the found digit
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: Reverse the part after the pivot index
        digits[i + 1:] = reversed(digits[i + 1:])
        
        # Convert list of digits back to integer
        result = int(''.join(digits))
        
        # Step 5: Check if the result is within the 32-bit signed integer range
        if result > 2**31 - 1:
            return -1
        
        return result
