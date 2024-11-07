class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # Transform the hours list into a list of +1 and -1
        # +1 for tiring days (hours > 8), -1 for non-tiring days (hours <= 8)
        score = [1 if h > 8 else -1 for h in hours]
        
        # Initialize a dictionary to store the first occurrence of each prefix sum
        prefix_sum_map = {}
        prefix_sum = 0  # This will track the running sum of the transformed array
        max_len = 0  # To store the length of the longest well-performing interval
        
        for i, s in enumerate(score):
            # Update the running prefix sum
            prefix_sum += s
            
            # If the current prefix sum is positive, the interval [0, i] is well-performing
            if prefix_sum > 0:
                max_len = i + 1  # Interval from the start to the current index
            
            # If not, check if we can find a previous prefix sum that allows a valid interval
            else:
                if (prefix_sum - 1) in prefix_sum_map:
                    max_len = max(max_len, i - prefix_sum_map[prefix_sum - 1])
            
            # Only store the first occurrence of the prefix sum in the map
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i
        
        return max_len
