class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        
        result = []
        while n != 0:
            remainder = n % -2
            n = n // -2
            
            # If remainder is negative, adjust it
            if remainder < 0:
                remainder += 2
                n += 1
            
            result.append(str(remainder))
        
        # Join the result in reverse order to form the correct binary string
        return ''.join(result[::-1])
