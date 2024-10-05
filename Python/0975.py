from typing import List
from collections import defaultdict
import bisect

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Edge case: single element array is always a valid starting point
        if n == 1:
            return 1
        
        # Next jump indices for odd and even jumps
        next_odd = [-1] * n
        next_even = [-1] * n
        
        # Compute the next odd jump index
        sorted_indices = sorted(range(n), key=lambda i: (arr[i], i))
        stack = []
        for index in sorted_indices:
            while stack and stack[-1] < index:
                next_odd[stack.pop()] = index
            stack.append(index)
        
        # Compute the next even jump index
        sorted_indices = sorted(range(n), key=lambda i: (-arr[i], i))
        stack = []
        for index in sorted_indices:
            while stack and stack[-1] < index:
                next_even[stack.pop()] = index
            stack.append(index)
        
        # Dynamic programming arrays to check reachability
        odd_jump = [False] * n
        even_jump = [False] * n
        
        # The last index is always reachable
        odd_jump[-1] = True
        even_jump[-1] = True
        
        # Fill DP arrays from right to left
        for i in range(n - 2, -1, -1):
            if next_odd[i] != -1:
                odd_jump[i] = even_jump[next_odd[i]]
            if next_even[i] != -1:
                even_jump[i] = odd_jump[next_even[i]]
        
        # Count valid starting indices
        return sum(odd_jump)
