from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Add indices to queries to track their order
        indexed_queries = [(preferred, minSize, idx) for idx, (preferred, minSize) in enumerate(queries)]
        
        # Sort queries by minSize in descending order, and preferred ID to simplify ties
        indexed_queries.sort(key=lambda x: (-x[1], x[0]))
        
        # Sort rooms by size in descending order
        rooms.sort(key=lambda x: -x[1])
        
        result = [-1] * len(queries)
        valid_rooms = SortedList()
        room_index = 0

        for preferred, minSize, idx in indexed_queries:
            # Add all rooms that satisfy the size condition
            while room_index < len(rooms) and rooms[room_index][1] >= minSize:
                valid_rooms.add(rooms[room_index][0])
                room_index += 1

            # Find the closest room using binary search
            if valid_rooms:
                pos = valid_rooms.bisect_left(preferred)

                closest_room = None
                closest_distance = float('inf')

                # Check the position at or after preferred
                if pos < len(valid_rooms):
                    candidate = valid_rooms[pos]
                    closest_distance = abs(candidate - preferred)
                    closest_room = candidate

                # Check the position before preferred
                if pos > 0:
                    candidate = valid_rooms[pos - 1]
                    if abs(candidate - preferred) < closest_distance or (
                        abs(candidate - preferred) == closest_distance and candidate < closest_room):
                        closest_room = candidate

                result[idx] = closest_room

        return result
