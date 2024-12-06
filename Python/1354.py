import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        
        # Convert to a max-heap (negate values since heapq is a min-heap)
        target = [-x for x in target]
        heapq.heapify(target)
        
        total_sum = -sum(target)
        
        while True:
            largest = -heapq.heappop(target)  # Get the largest element
            total_sum -= largest  # Calculate the sum of the rest of the elements
            
            # If the largest element is already 1 or total_sum is 1, we can stop
            if largest == 1 or total_sum == 1:
                return True
            
            # If it's impossible to proceed
            if total_sum == 0 or largest < total_sum or largest % total_sum == 0:
                return False
            
            # Reduce the largest element
            largest %= total_sum
            total_sum += largest  # Update the total sum
            
            # Push the new value back into the heap
            heapq.heappush(target, -largest)
