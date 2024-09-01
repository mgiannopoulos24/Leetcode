class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # Adjust columnNumber to be zero-indexed
            columnNumber -= 1
            
            # Determine the current letter
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))
            
            # Move to the next significant digit
            columnNumber //= 26
        
        # Reverse the result list to get the correct order
        return ''.join(result[::-1])
