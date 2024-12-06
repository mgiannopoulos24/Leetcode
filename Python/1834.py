from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Step 1: Prepare tasks with indices and sort by enqueue time
        tasks_with_index = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        tasks_with_index.sort()
        
        # Step 2: Initialize variables
        result = []
        min_heap = []
        time = 0
        i = 0
        n = len(tasks)
        
        # Step 3: Process tasks until all are handled
        while len(result) < n:
            # Add all tasks that are now available to the heap
            while i < n and tasks_with_index[i][0] <= time:
                enqueue_time, processing_time, index = tasks_with_index[i]
                heapq.heappush(min_heap, (processing_time, index))
                i += 1
            
            if min_heap:
                # If there are tasks in the heap, process the one with smallest processing time (and smallest index in case of tie)
                processing_time, index = heapq.heappop(min_heap)
                time += processing_time
                result.append(index)
            else:
                # No tasks are available; move time to the next available task's enqueue time
                time = tasks_with_index[i][0]
        
        return result
