from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Step 1: Flip each row horizontally
        flipped_image = [row[::-1] for row in image]
        
        # Step 2: Invert each element in the flipped image
        inverted_image = [[1 - pixel for pixel in row] for row in flipped_image]
        
        return inverted_image
