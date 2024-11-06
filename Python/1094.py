class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        
        # For each trip, we record two events: pickup and drop-off
        for num_passengers, start, end in trips:
            events.append((start, num_passengers))  # Picking up passengers at 'start'
            events.append((end, -num_passengers))   # Dropping off passengers at 'end'
        
        # Sort the events by location (if same location, pickups should come before drop-offs)
        events.sort(key=lambda x: (x[0], x[1]))
        
        # Track the number of passengers currently in the car
        current_passengers = 0
        
        # Process each event
        for location, passenger_change in events:
            current_passengers += passenger_change
            # Check if capacity is exceeded
            if current_passengers > capacity:
                return False
        
        # If we managed all events without exceeding capacity, return True
        return True
