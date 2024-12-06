class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        import math

        def can_arrive(speed: int) -> bool:
            total_time = 0
            for i in range(len(dist) - 1):
                total_time += math.ceil(dist[i] / speed)
            total_time += dist[-1] / speed
            return total_time <= hour

        left, right = 1, 10**7
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if can_arrive(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
