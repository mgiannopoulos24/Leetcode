class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total_sum = 0
        
        while n > 0:
            digit = n % 10  # Extract the last digit
            product *= digit  # Update the product
            total_sum += digit  # Update the sum
            n //= 10  # Remove the last digit
        
        return product - total_sum
