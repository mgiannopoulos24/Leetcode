import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # Step 1: Make all numbers even, multiply odd numbers by 2
        heap = []
        min_val = float('inf')
        
        for num in nums:
            if num % 2 == 1:
                num *= 2  # Make odd numbers even
            heapq.heappush(heap, -num)  # Push into heap (negative because heapq is a min-heap)
            min_val = min(min_val, num)  # Track the minimum value in the array
        
        # Step 2: Minimize deviation
        deviation = float('inf')
        
        while heap:
            max_val = -heapq.heappop(heap)  # Get the largest element (remember it was negated)
            deviation = min(deviation, max_val - min_val)  # Update the minimum deviation
            
            if max_val % 2 == 0:
                max_val //= 2  # Divide the largest element by 2
                min_val = min(min_val, max_val)  # Update the minimum value
                heapq.heappush(heap, -max_val)  # Push the reduced element back into the heap
            else:
                # If the largest number is odd, stop as we can't reduce it further
                break
        
        return deviation
