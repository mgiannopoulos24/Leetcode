class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Create a set to store all cities with outgoing paths (cityAi)
        outgoing_cities = set()
        
        # Populate the outgoing cities set
        for path in paths:
            outgoing_cities.add(path[0])
        
        # Check each cityBi, the destination city, and return the one not in outgoing_cities
        for path in paths:
            if path[1] not in outgoing_cities:
                return path[1]