from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create a list of tuples where each tuple is (capital required, profit)
        projects = list(zip(capital, profits))
        
        # Min-heap to store projects by their capital requirement
        min_capital_heap = []
        
        # Max-heap to store profits of projects that can be started with the current capital
        max_profit_heap = []
        
        # Push all projects into the min-heap
        for cap, prof in projects:
            heapq.heappush(min_capital_heap, (cap, prof))
        
        # Iterate up to k times to select projects
        for _ in range(k):
            # Push all projects that can be started with current capital into max-profit heap
            while min_capital_heap and min_capital_heap[0][0] <= w:
                cap, prof = heapq.heappop(min_capital_heap)
                heapq.heappush(max_profit_heap, -prof)  # Push negative to simulate max-heap using min-heap
            
            # If no projects can be started, break early
            if not max_profit_heap:
                break
            
            # Pop the project with the maximum profit from the max-heap
            w -= heapq.heappop(max_profit_heap)  # Subtract because profits are stored as negative
        
        return w
