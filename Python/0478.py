import random
import math
from typing import List

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # Generate a random radius
        r = math.sqrt(random.uniform(0, 1)) * self.radius
        # Generate a random angle
        theta = random.uniform(0, 2 * math.pi)
        
        # Convert polar coordinates to Cartesian coordinates
        x = r * math.cos(theta) + self.x_center
        y = r * math.sin(theta) + self.y_center
        
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()