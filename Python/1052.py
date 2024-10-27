class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Calculate the base satisfaction where the owner is not grumpy
        base_satisfaction = 0
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfaction += customers[i]
        
        # Now calculate the additional customers we could satisfy by using the technique
        # for exactly 'minutes' length of time, where the owner is grumpy.
        max_additional_satisfaction = 0
        additional_satisfaction = 0
        
        # Sliding window to calculate the additional satisfaction we can gain in 'minutes' window
        for i in range(n):
            if grumpy[i] == 1:
                additional_satisfaction += customers[i]
            
            # If the window exceeds the 'minutes', subtract the customers who are now outside the window
            if i >= minutes and grumpy[i - minutes] == 1:
                additional_satisfaction -= customers[i - minutes]
            
            # Keep track of the maximum additional satisfaction we can gain
            max_additional_satisfaction = max(max_additional_satisfaction, additional_satisfaction)
        
        # The total satisfied customers is the base satisfaction plus the maximum possible additional satisfaction
        return base_satisfaction + max_additional_satisfaction
