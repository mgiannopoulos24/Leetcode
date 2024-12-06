class Solution:
    def totalMoney(self, n: int) -> int:
        # Calculate full weeks and remaining days
        full_weeks = n // 7
        remaining_days = n % 7
        
        # Sum of deposits for all full weeks
        # Each full week sum can be computed as: 7 * starting_amount + sum of first 7 numbers (21)
        # Using the formula for sum of arithmetic series over weeks
        full_weeks_sum = (full_weeks * (2 + (full_weeks - 1))) * 7 // 2 + 21 * full_weeks
        
        # Sum of deposits for the remaining days
        remaining_sum = sum(full_weeks + 1 + i for i in range(remaining_days))
        
        # Total money after n days
        return full_weeks_sum + remaining_sum
