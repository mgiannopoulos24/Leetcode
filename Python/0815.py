from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # Step 1: Build the graph
        bus_stop_to_buses = defaultdict(set)
        bus_to_stops = defaultdict(list)
        
        for bus, stops in enumerate(routes):
            for stop in stops:
                bus_stop_to_buses[stop].add(bus)
                bus_to_stops[bus].append(stop)
        
        # Step 2: BFS initialization
        visited_stops = set()
        visited_buses = set()
        queue = deque([(source, 0)])  # (current_stop, number_of_buses_taken)
        
        while queue:
            current_stop, num_buses = queue.popleft()
            
            for bus in bus_stop_to_buses[current_stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                
                for stop in bus_to_stops[bus]:
                    if stop == target:
                        return num_buses + 1
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop, num_buses + 1))
        
        return -1
