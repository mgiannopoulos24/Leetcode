class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Stack to maintain the indices of prices
        stack = []
        # Initialize the answer array as a copy of the original prices
        answer = prices[:]
        
        for i in range(len(prices)):
            # While there is an item in the stack and the current price is less than or equal to the price
            # at the top index of the stack, apply the discount
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                answer[index] = prices[index] - prices[i]
            
            # Push the current index onto the stack
            stack.append(i)
        
        return answer
