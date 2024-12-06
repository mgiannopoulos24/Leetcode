class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n == 1:
            return arr[0]
        
        # Initialize the arrays
        no_deletion = [0] * n
        one_deletion = [0] * n
        
        no_deletion[0] = arr[0]
        one_deletion[0] = float('-inf')  # Impossible to delete the first element
        
        max_sum = arr[0]
        
        for i in range(1, n):
            # Maximum subarray sum ending at i without deletion
            no_deletion[i] = max(arr[i], no_deletion[i-1] + arr[i])
            
            # Maximum subarray sum ending at i with one deletion
            one_deletion[i] = max(one_deletion[i-1] + arr[i], no_deletion[i-1])
            
            # Track the maximum of no_deletion[i] and one_deletion[i]
            max_sum = max(max_sum, no_deletion[i], one_deletion[i])
        
        return max_sum
