class UndergroundSystem:

    def __init__(self):
        # Stores check-in information: id -> (stationName, time)
        self.check_in_info = {}
        
        # Stores total travel time and number of trips for station pairs
        # (startStation, endStation) -> (total_time, trip_count)
        self.trip_data = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Store the check-in information for the customer
        self.check_in_info[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Retrieve the check-in information
        start_station, start_time = self.check_in_info.pop(id)
        
        # Calculate the travel time
        travel_time = t - start_time
        
        # Update the trip_data for the pair (start_station, stationName)
        if (start_station, stationName) not in self.trip_data:
            self.trip_data[(start_station, stationName)] = (travel_time, 1)
        else:
            total_time, trip_count = self.trip_data[(start_station, stationName)]
            self.trip_data[(start_station, stationName)] = (total_time + travel_time, trip_count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Retrieve the total time and trip count for the station pair
        total_time, trip_count = self.trip_data[(startStation, endStation)]
        
        # Return the average time
        return total_time / trip_count



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)