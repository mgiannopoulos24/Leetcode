from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_duration = 0
        end = 0  # End time of the current poison effect

        for time in timeSeries:
            if time > end:
                # New poison interval starts
                total_duration += duration
            else:
                # Poison interval extends
                total_duration += (time + duration - end)
            # Update the end of the poison effect
            end = time + duration

        return total_duration
