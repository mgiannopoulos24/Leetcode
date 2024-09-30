from heapq import heappush, heappop
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Add a final station at the target with zero fuel
        stations.append([target, 0])
        
        # Max-heap to keep track of the fuel from past stations
        max_heap = []
        
        # Current fuel and position
        current_fuel = startFuel
        current_position = 0
        stops = 0
        
        for position, fuel in stations:
            distance_to_station = position - current_position
            
            # If current fuel cannot reach the next station, refuel from past stations
            while current_fuel < distance_to_station:
                if not max_heap:
                    return -1  # Not possible to reach the target
                # Refuel from the station with the maximum fuel available
                current_fuel += -heappop(max_heap)
                stops += 1
            
            # Move to the next station
            current_fuel -= distance_to_station
            current_position = position
            # Add this station's fuel to the max-heap
            heappush(max_heap, -fuel)
        
        return stops
