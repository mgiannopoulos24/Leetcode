import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Pair up efficiency and speed, and sort by efficiency in descending order
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        max_performance = 0
        speed_sum = 0
        speed_heap = []
        
        for curr_efficiency, curr_speed in engineers:
            # Add current speed to the heap (min-heap to track the top k speeds)
            heapq.heappush(speed_heap, curr_speed)
            speed_sum += curr_speed
            
            # If we have more than k engineers, remove the one with the lowest speed
            if len(speed_heap) > k:
                speed_sum -= heapq.heappop(speed_heap)
            
            # Calculate the performance with the current engineer's efficiency as the minimum
            max_performance = max(max_performance, speed_sum * curr_efficiency)
        
        return max_performance % MOD
