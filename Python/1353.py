import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events by their start day
        events.sort()
        
        # Determine the last day when any event ends
        total_days = max(event[1] for event in events)
        
        event_index = 0
        max_events = 0
        min_heap = []
        
        # Step 2: Iterate over each day from day 1 to the last day when any event ends
        for day in range(1, total_days + 1):
            # Add all events that start on the current day or earlier to the heap
            while event_index < len(events) and events[event_index][0] <= day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1
            
            # Remove events from the heap that have already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # Attend the event that ends the earliest (smallest end time)
            if min_heap:
                heapq.heappop(min_heap)
                max_events += 1
        
        return max_events
