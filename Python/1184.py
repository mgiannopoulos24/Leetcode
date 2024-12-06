class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # Ensure that start is less than destination for easier calculation
        if start > destination:
            start, destination = destination, start
        
        # Step 1: Calculate the clockwise distance
        clockwise_distance = sum(distance[start:destination])
        
        # Step 2: Calculate the total distance around the circle
        total_distance = sum(distance)
        
        # Step 3: Calculate the counterclockwise distance
        counterclockwise_distance = total_distance - clockwise_distance
        
        # Step 4: Return the minimum of the two distances
        return min(clockwise_distance, counterclockwise_distance)
