class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Compute prefix XOR array
        n = len(arr)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        # Step 2: Answer the queries
        result = []
        for left, right in queries:
            # XOR of elements from left to right is prefix[right + 1] ^ prefix[left]
            result.append(prefix[right + 1] ^ prefix[left])
        
        return result
