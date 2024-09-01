class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        # Try all pairs of first and second number lengths
        for i in range(1, n):
            for j in range(i + 1, n):
                num1 = num[:i]
                num2 = num[i:j]
                
                # Skip numbers with leading zeros
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                
                # Convert substrings to integers
                x1, x2 = int(num1), int(num2)
                start = j
                
                while start < n:
                    # Next number in the sequence
                    x3 = x1 + x2
                    x3_str = str(x3)
                    x3_len = len(x3_str)
                    
                    # Check if the next part of num matches x3
                    if not num.startswith(x3_str, start):
                        break
                    
                    # Move forward in the sequence
                    start += x3_len
                    x1, x2 = x2, x3
                    
                # If we've gone through the whole string, return True
                if start == n:
                    return True
                
        # If no valid sequence is found, return False
        return False



