from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(target: int) -> int:
            rotations_top = rotations_bottom = 0
            
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    # If neither top nor bottom at position i is the target, it's impossible
                    return -1
                elif tops[i] != target:
                    # If top is not the target, we need to rotate the top
                    rotations_top += 1
                elif bottoms[i] != target:
                    # If bottom is not the target, we need to rotate the bottom
                    rotations_bottom += 1
            
            # Return the minimum rotations between top and bottom
            return min(rotations_top, rotations_bottom)
        
        # Check the two possible targets: tops[0] or bottoms[0]
        rotations = check(tops[0])
        if rotations != -1:
            return rotations
        # If tops[0] is not possible, try bottoms[0]
        return check(bottoms[0])
