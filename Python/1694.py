class Solution:
    def reformatNumber(self, number: str) -> str:
        # Step 1: Remove all spaces and dashes
        digits = [ch for ch in number if ch.isdigit()]
        
        # Step 2: Create the result list
        result = []
        i = 0
        n = len(digits)
        
        # Step 3: Group digits into blocks
        while n - i > 4:
            result.append(''.join(digits[i:i+3]))
            i += 3
        
        # Handle the last 2-4 digits
        if n - i == 4:
            result.append(''.join(digits[i:i+2]))
            result.append(''.join(digits[i+2:i+4]))
        else:
            result.append(''.join(digits[i:]))
        
        # Step 4: Join the result with dashes
        return '-'.join(result)
