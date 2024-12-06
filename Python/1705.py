import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # Priority queue to store (rot_day, apples_left) as a tuple
        pq = []
        day = 0
        total_apples_eaten = 0

        while day < len(apples) or pq:
            # If apples grow on the current day, add them to the queue
            if day < len(apples) and apples[day] > 0:
                heapq.heappush(pq, (day + days[day], apples[day]))

            # Remove rotten apples or empty entries from the queue
            while pq and (pq[0][0] <= day or pq[0][1] == 0):
                heapq.heappop(pq)

            # Eat one apple from the freshest available batch (with earliest rotting day)
            if pq:
                rot_day, apple_count = heapq.heappop(pq)
                total_apples_eaten += 1
                if apple_count > 1:
                    heapq.heappush(pq, (rot_day, apple_count - 1))

            day += 1

        return total_apples_eaten
