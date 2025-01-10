from collections import defaultdict

class DetectSquares:

    def __init__(self):
        # Use a nested dictionary to store points and their frequencies
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1  # Increment the count of this point

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0

        # Iterate over all points with the same x-coordinate
        for y1 in self.points[x]:
            if y1 == y:
                continue  # Skip the query point itself

            # Calculate the side length of the square
            d = abs(y1 - y)

            # Check for the other two points to form a square
            # Case 1: Points are to the right of the query point
            if x + d in self.points:
                count += self.points[x + d][y] * self.points[x + d][y1] * self.points[x][y1]

            # Case 2: Points are to the left of the query point
            if x - d in self.points:
                count += self.points[x - d][y] * self.points[x - d][y1] * self.points[x][y1]

        return count
