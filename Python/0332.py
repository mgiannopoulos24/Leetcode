from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Build the graph with a priority queue for each adjacency list
        graph = defaultdict(list)
        for frm, to in tickets:
            heapq.heappush(graph[frm], to)
        
        # Step 2: Define a DFS function to build the itinerary
        def dfs(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            itinerary.append(airport)
        
        # Step 3: Initialize the itinerary and start DFS from 'JFK'
        itinerary = []
        dfs('JFK')
        
        # Step 4: Since the itinerary is constructed in reverse, reverse it before returning
        return itinerary[::-1]