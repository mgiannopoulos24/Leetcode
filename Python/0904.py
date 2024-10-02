from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        max_fruits = 0
        basket = defaultdict(int)  # To keep track of fruit counts in the current window

        for end in range(len(fruits)):
            fruit = fruits[end]
            basket[fruit] += 1
            
            # If there are more than two types of fruits in the basket, shrink the window
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            
            # Calculate the current window size
            current_window_size = end - start + 1
            max_fruits = max(max_fruits, current_window_size)

        return max_fruits
