class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # Step 1: Generate all Fibonacci numbers <= k
        fibs = [1, 1]  # Start with the first two Fibonacci numbers
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])
        
        # Step 2: Greedily subtract the largest Fibonacci numbers
        count = 0
        i = len(fibs) - 1
        
        while k > 0:
            if fibs[i] <= k:
                k -= fibs[i]
                count += 1
            i -= 1
        
        return count
