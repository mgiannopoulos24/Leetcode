import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Step 1: Calculate initial gain and use a max heap to store negative gains for each class
        heap = []
        
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t
        
        for p, t in classes:
            # Push negative gain to simulate a max-heap
            heapq.heappush(heap, (-gain(p, t), p, t))
        
        # Step 2: Distribute each extra student to the class with the highest gain
        for _ in range(extraStudents):
            current_gain, p, t = heapq.heappop(heap)
            # Update the class by adding one passing student
            p += 1
            t += 1
            # Push the updated gain back into the heap
            heapq.heappush(heap, (-gain(p, t), p, t))
        
        # Step 3: Calculate the final average pass ratio
        total_ratio = 0
        for _, p, t in heap:
            total_ratio += p / t
        
        return total_ratio / len(classes)
