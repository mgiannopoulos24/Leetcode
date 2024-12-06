class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # Initialize the minimum and maximum values for the four possible expressions
        max1 = max2 = max3 = max4 = float('-inf')
        min1 = min2 = min3 = min4 = float('inf')
        
        # Loop over the array indices and calculate the four expressions
        for i in range(len(arr1)):
            expr1 = arr1[i] + arr2[i] + i
            expr2 = arr1[i] + arr2[i] - i
            expr3 = arr1[i] - arr2[i] + i
            expr4 = arr1[i] - arr2[i] - i
            
            # Update min and max for each expression
            max1 = max(max1, expr1)
            min1 = min(min1, expr1)
            
            max2 = max(max2, expr2)
            min2 = min(min2, expr2)
            
            max3 = max(max3, expr3)
            min3 = min(min3, expr3)
            
            max4 = max(max4, expr4)
            min4 = min(min4, expr4)
        
        # Calculate the maximum difference for each of the four expressions
        result = max(max1 - min1, max2 - min2, max3 - min3, max4 - min4)
        
        return result
