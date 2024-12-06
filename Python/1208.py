class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        left = 0  # Left pointer for the sliding window
        total_cost = 0  # Accumulated cost of the current window
        max_len = 0  # Store the maximum length of a valid window
        
        # Sliding window approach
        for right in range(n):
            # Calculate the cost of changing s[right] to t[right]
            total_cost += abs(ord(s[right]) - ord(t[right]))
            
            # If the total cost exceeds maxCost, shrink the window from the left
            while total_cost > maxCost:
                total_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            # Update the maximum valid window length
            max_len = max(max_len, right - left + 1)
        
        return max_len
