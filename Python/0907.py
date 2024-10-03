from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # Arrays to store the number of subarrays where arr[i] is the minimum
        left = [0] * n
        right = [0] * n
        
        # Monotonic stack approach to fill left array
        stack = []
        for i in range(n):
            # Elements in stack are indices in increasing order of their values in arr
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                left[i] = i - stack[-1]
            else:
                left[i] = i + 1
            stack.append(i)
        
        # Clear stack for calculating right array
        stack = []
        for i in range(n-1, -1, -1):
            # Elements in stack are indices in increasing order of their values in arr
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1] - i
            else:
                right[i] = n - i
            stack.append(i)
        
        # Calculate the sum of all minimums
        result = 0
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % MOD
        
        return result