class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # Total count of all numbers
        total_count = sum(count)
        
        # Initialize variables for statistics
        minimum = None
        maximum = None
        total_sum = 0
        mode = None
        mode_count = 0
        running_count = 0  # Running count to help with median calculation
        
        # First pass to get min, max, sum, mode
        for i in range(256):
            if count[i] > 0:
                # Minimum value
                if minimum is None:
                    minimum = i
                # Maximum value
                maximum = i
                # Update total sum
                total_sum += i * count[i]
                # Mode
                if count[i] > mode_count:
                    mode = i
                    mode_count = count[i]
        
        # Second pass to calculate the median
        median = 0
        mid1 = (total_count + 1) // 2  # First middle for odd/even cases
        mid2 = (total_count + 2) // 2  # Second middle for even cases
        
        current_count = 0
        for i in range(256):
            current_count += count[i]
            # If we find mid1 (odd or first middle of even)
            if current_count >= mid1 and median == 0:
                median = i
            # If we find mid2 (second middle of even case)
            if current_count >= mid2:
                if total_count % 2 == 0:
                    median = (median + i) / 2
                break
        
        # Calculate the mean
        mean = total_sum / total_count
        
        # Return the results in the required format
        return [float(minimum), float(maximum), float(mean), float(median), float(mode)]
