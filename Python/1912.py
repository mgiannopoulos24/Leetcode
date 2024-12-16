from sortedcontainers import SortedList
from typing import List

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented = {}  # {movie: SortedList of (price, shop)}
        self.rented = SortedList()  # SortedList of (price, shop, movie)
        self.prices = {}  # (shop, movie): price

        for shop, movie, price in entries:
            if movie not in self.unrented:
                self.unrented[movie] = SortedList()
            self.unrented[movie].add((price, shop))
            self.prices[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self.unrented:
            return []
        # Return the first 5 shops with the movie
        return [shop for _, shop in self.unrented[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.unrented[movie].remove((price, shop))  # Remove from unrented
        self.rented.add((price, shop, movie))  # Add to rented

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))  # Remove from rented
        self.unrented[movie].add((price, shop))  # Add back to unrented

    def report(self) -> List[List[int]]:
        # Return the first 5 rented movies
        return [[shop, movie] for _, shop, movie in self.rented[:5]]



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()