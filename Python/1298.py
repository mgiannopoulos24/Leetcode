from typing import List
from collections import deque

class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int]
    ) -> int:
        n = len(status)
        
        # Sets to keep track of states
        opened_boxes = set()      # Boxes that have been opened
        available_keys = set()    # Keys that have been collected
        boxes_waiting = set()     # Boxes that are closed and waiting for a key
        
        # Initialize the queue for BFS
        queue = deque()
        
        # Total candies collected
        total_candies = 0
        
        # Function to attempt opening a box
        def try_open_box(box):
            if box in opened_boxes:
                # Already opened, skip
                return
            if status[box] == 1 or box in available_keys:
                # Box is open or we have a key to open it
                opened_boxes.add(box)
                total = candies[box]
                nonlocal total_candies
                total_candies += total
                # Add keys from this box
                for key in keys[box]:
                    if key not in available_keys:
                        available_keys.add(key)
                        # If the key opens a box waiting to be opened, enqueue it
                        if key in boxes_waiting:
                            queue.append(key)
                            boxes_waiting.remove(key)
                # Add contained boxes to the queue
                for contained_box in containedBoxes[box]:
                    if contained_box in opened_boxes:
                        # Already opened, skip
                        continue
                    if status[contained_box] == 1 or contained_box in available_keys:
                        queue.append(contained_box)
                    else:
                        boxes_waiting.add(contained_box)
            else:
                # Box is closed and we don't have a key yet
                boxes_waiting.add(box)
        
        # Initialize by trying to open all initial boxes
        for box in initialBoxes:
            try_open_box(box)
        
        # BFS traversal
        while queue:
            current_box = queue.popleft()
            try_open_box(current_box)
        
        return total_candies
