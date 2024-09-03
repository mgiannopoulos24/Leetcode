from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Get the length of the score array
        n = len(score)
        
        # Sort the scores in descending order and keep the original indices
        sorted_scores = sorted(range(n), key=lambda x: score[x], reverse=True)
        
        # Initialize the result array with empty strings
        result = [""] * n
        
        # Assign ranks based on sorted positions
        for i, idx in enumerate(sorted_scores):
            if i == 0:
                result[idx] = "Gold Medal"
            elif i == 1:
                result[idx] = "Silver Medal"
            elif i == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(i + 1)
        
        return result
