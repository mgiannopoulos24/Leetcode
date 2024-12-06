class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        prefixXOR = [0] * (n + 1)  # Prefix XOR array
        
        # Compute prefix XOR
        for i in range(n):
            prefixXOR[i + 1] = prefixXOR[i] ^ arr[i]
        
        # Iterate over all pairs (i, k) where i < k
        for i in range(n):
            for k in range(i + 1, n):
                # If prefixXOR[i] == prefixXOR[k + 1], then the XOR from i to k is 0
                if prefixXOR[i] == prefixXOR[k + 1]:
                    # For this (i, k), any j such that i < j <= k will be valid
                    count += (k - i)
        
        return count
