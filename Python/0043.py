class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)  # Result can have at most len1 + len2 digits
        
        # Perform digit-by-digit multiplication
        for i in reversed(range(len1)):
            for j in reversed(range(len2)):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2
                
                # Add current product to the appropriate position in result
                pos1 = i + j
                pos2 = i + j + 1
                total = product + result[pos2]
                
                result[pos1] += total // 10  # Carry
                result[pos2] = total % 10  # Digit result
        
        # Convert result list to string
        result_str = "".join(map(str, result))
        
        # Remove leading zeros
        result_str = result_str.lstrip("0")
        
        return result_str if result_str else "0"
