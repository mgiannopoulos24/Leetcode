class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Compute the wealth for each customer and return the maximum wealth
        return max([sum(customer) for customer in accounts])
