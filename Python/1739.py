class Solution:
    def minimumBoxes(self, n: int) -> int:
        # Find the max possible layer where cumulative boxes are <= n
        k = 0
        total_boxes = 0
        while total_boxes < n:
            k += 1
            total_boxes += k * (k + 1) // 2
        
        # Adjust if we overshot
        if total_boxes > n:
            total_boxes -= k * (k + 1) // 2
            k -= 1
        
        # Now count the floor boxes in the last layer until we reach n
        extra_boxes = n - total_boxes
        floor_boxes = k * (k + 1) // 2
        next_layer = 1
        
        while extra_boxes > 0:
            floor_boxes += 1
            extra_boxes -= next_layer
            next_layer += 1
        
        return floor_boxes
