import math

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def calculate_quality(x, y):
            total_quality = 0
            for tx, ty, tq in towers:
                # Calculate the Euclidean distance between (x, y) and the tower (tx, ty)
                distance = math.sqrt((tx - x) ** 2 + (ty - y) ** 2)
                # If the tower is within the radius, calculate its contribution to the total quality
                if distance <= radius:
                    total_quality += math.floor(tq / (1 + distance))
            return total_quality
        
        best_quality = -1
        best_coordinate = [0, 0]
        
        # Iterate over all possible coordinates in the range [0, 50] for both x and y
        for x in range(51):
            for y in range(51):
                quality = calculate_quality(x, y)
                if quality > best_quality:
                    best_quality = quality
                    best_coordinate = [x, y]
                elif quality == best_quality:
                    # Choose lexicographically smaller coordinate
                    if [x, y] < best_coordinate:
                        best_coordinate = [x, y]
        
        return best_coordinate
