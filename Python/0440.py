class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1  # Since we start from 1 and need to find the k-th, decrement k by 1

        while k > 0:
            count = self.countNumbers(n, current)
            if count <= k:
                # If there are fewer or exactly k numbers, move to the next prefix
                current += 1
                k -= count
            else:
                # If there are more than k numbers, go deeper
                current *= 10
                k -= 1

        return current
    
    def countNumbers(self, n: int, prefix: int) -> int:
        count = 0
        curr = prefix
        next_prefix = prefix + 1
        
        while curr <= n:
            count += min(n + 1, next_prefix) - curr
            curr *= 10
            next_prefix *= 10
        
        return count
