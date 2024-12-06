class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # Step 1: Filter the restaurants based on the given criteria
        filtered_restaurants = []
        for restaurant in restaurants:
            id, rating, vegan, price, distance = restaurant
            if (veganFriendly == 0 or vegan == 1) and price <= maxPrice and distance <= maxDistance:
                filtered_restaurants.append(restaurant)
        
        # Step 2: Sort by rating first, and by id if ratings are the same
        filtered_restaurants.sort(key=lambda x: (x[1], x[0]), reverse=True)
        
        # Step 3: Return only the ids of the sorted restaurants
        return [restaurant[0] for restaurant in filtered_restaurants]
