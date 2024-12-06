from typing import List

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Counts the number of odd numbers between low and high (inclusive).

        Parameters:
        - low (int): The lower bound of the range.
        - high (int): The upper bound of the range.

        Returns:
        - int: The count of odd numbers within the range.
        """
        # Calculate the number of odd numbers up to high
        odds_up_to_high = (high + 1) // 2
        
        # Calculate the number of odd numbers below low
        odds_below_low = low // 2
        
        # The total number of odd numbers in [low, high] is the difference
        total_odds = odds_up_to_high - odds_below_low
        
        return total_odds
