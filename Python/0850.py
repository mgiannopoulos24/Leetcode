class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Extract and compress coordinates
        x_coords = set()
        y_coords = set()
        
        for x1, y1, x2, y2 in rectangles:
            x_coords.add(x1)
            x_coords.add(x2)
            y_coords.add(y1)
            y_coords.add(y2)
        
        x_sorted = sorted(x_coords)
        y_sorted = sorted(y_coords)
        
        x_map = {x: i for i, x in enumerate(x_sorted)}
        y_map = {y: i for i, y in enumerate(y_sorted)}
        
        # Step 2: Create event list
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x_map[x1], y_map[y1], y_map[y2], 1))  # Start of rectangle
            events.append((x_map[x2], y_map[y1], y_map[y2], -1)) # End of rectangle
        
        # Sort events by x-coordinate
        events.sort()
        
        # Step 3: Sweep line algorithm
        last_x = 0
        active_intervals = [0] * (len(y_sorted) - 1)
        area = 0
        
        def calculate_y_length():
            length = 0
            for i, count in enumerate(active_intervals):
                if count > 0:
                    length += y_sorted[i + 1] - y_sorted[i]
            return length
        
        for x, y1, y2, typ in events:
            current_x = x_sorted[x]
            y_length = calculate_y_length()
            area += y_length * (current_x - last_x)
            area %= MOD
            
            for i in range(y1, y2):
                active_intervals[i] += typ
            
            last_x = current_x
        
        return area
