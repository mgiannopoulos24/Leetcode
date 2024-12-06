from heapq import heappush, heappop

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by their start time
        intervals.sort()
        
        # Pair each query with its index for tracking order
        indexed_queries = sorted((q, i) for i, q in enumerate(queries))

        result = [-1] * len(queries)
        min_heap = []
        i = 0

        for query, idx in indexed_queries:
            # Add all intervals that start before or at the current query
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heappush(min_heap, (right - left + 1, right, left))
                i += 1

            # Remove intervals that end before the current query
            while min_heap and min_heap[0][1] < query:
                heappop(min_heap)

            # If the heap is not empty, the top element is the smallest valid interval
            if min_heap:
                result[idx] = min_heap[0][0]

        return result
