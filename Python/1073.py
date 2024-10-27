class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Helper function to convert a base -2 array to a decimal integer
        def baseNeg2ToDecimal(arr):
            n = 0
            for i, bit in enumerate(reversed(arr)):
                n += bit * ((-2) ** i)
            return n
        
        # Helper function to convert a decimal integer to a base -2 array
        def decimalToBaseNeg2(num):
            if num == 0:
                return [0]
            result = []
            while num != 0:
                remainder = num % -2
                num = num // -2
                
                # Adjust remainder to be positive (0 or 1)
                if remainder < 0:
                    remainder += 2
                    num += 1
                
                result.append(remainder)
            
            return result[::-1]
        
        # Convert both arrays to decimal
        num1 = baseNeg2ToDecimal(arr1)
        num2 = baseNeg2ToDecimal(arr2)
        
        # Add the two numbers
        total = num1 + num2
        
        # Convert the result back to base -2
        return decimalToBaseNeg2(total)
