class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_i_value = values[0]  # Initial max value of values[i] + i
        
        for j in range(1, len(values)):
            # Calculate the score for the current pair (i, j) where i < j
            max_score = max(max_score, max_i_value + values[j] - j)
            
            # Update max_i_value to be the maximum of values[i] + i for future j
            max_i_value = max(max_i_value, values[j] + j)
        
        return max_score
