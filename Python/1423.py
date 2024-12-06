class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)  # Total sum of all the card points
        
        # Special case: if k == n, take all cards
        if k == n:
            return total_sum
        
        # Find the minimum sum subarray of length n - k
        window_size = n - k
        current_window_sum = sum(cardPoints[:window_size])
        min_window_sum = current_window_sum
        
        # Slide the window across the array to find the minimum sum
        for i in range(window_size, n):
            current_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, current_window_sum)
        
        # Maximum score is total sum minus the minimum sum of the subarray we leave
        return total_sum - min_window_sum