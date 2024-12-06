from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Keeps track of when each server becomes available
        available_servers = SortedList(range(k))
        
        # Min-heap to track when servers will become available again
        busy_servers = []
        
        # To count the number of requests handled by each server
        request_count = [0] * k
        
        for i in range(len(arrival)):
            # Current request arrival time and load time
            start_time = arrival[i]
            duration = load[i]
            end_time = start_time + duration
            
            # Free all servers whose end time is less than or equal to current start time
            while busy_servers and busy_servers[0][0] <= start_time:
                _, server_id = heapq.heappop(busy_servers)
                available_servers.add(server_id)
            
            if len(available_servers) == 0:
                # All servers are busy, skip this request
                continue
            
            # Find the next available server starting from i % k
            idx = available_servers.bisect_left(i % k)
            if idx == len(available_servers):
                idx = 0  # Wrap around if necessary
            server_id = available_servers[idx]
            
            # Assign the request to this server
            available_servers.remove(server_id)
            heapq.heappush(busy_servers, (end_time, server_id))
            request_count[server_id] += 1
        
        # Find the maximum number of requests handled by any server
        max_requests = max(request_count)
        
        # Return the list of servers that handled the maximum number of requests
        return [i for i in range(k) if request_count[i] == max_requests]
