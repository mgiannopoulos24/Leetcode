class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)
        
        # Memoization table to store the result of dp(city, fuel_left)
        memo = {}

        def dp(city, fuel_left):
            # If the result has been computed, return it
            if (city, fuel_left) in memo:
                return memo[(city, fuel_left)]
            
            # Base case: if fuel is negative, no valid route
            if fuel_left < 0:
                return 0
            
            # Base case: if we are at the finish, this is a valid route
            result = 1 if city == finish else 0
            
            # Try moving to all other cities
            for next_city in range(n):
                if next_city != city:
                    cost = abs(locations[city] - locations[next_city])
                    if fuel_left >= cost:
                        result += dp(next_city, fuel_left - cost)
                        result %= MOD
            
            # Memoize and return the result
            memo[(city, fuel_left)] = result
            return result
        
        # Start the recursion from the start city with the initial fuel
        return dp(start, fuel)
