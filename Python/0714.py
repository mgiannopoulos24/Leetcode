from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        cash = 0
        hold = float('-inf')
        
        for price in prices:
            # Update cash state: either continue without holding or sell the stock we held
            cash = max(cash, hold + price - fee)
            # Update hold state: either continue holding or buy stock at current price
            hold = max(hold, cash - price)
        
        return cash
