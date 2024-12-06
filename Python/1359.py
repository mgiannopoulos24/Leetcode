MOD = 10**9 + 7

class Solution:
    def countOrders(self, n: int) -> int:
        # Initialize the result for 1 order
        result = 1
        
        # Use the recursive formula for each number of orders from 2 to n
        for i in range(2, n + 1):
            result = result * i * (2 * i - 1) % MOD
        
        return result
