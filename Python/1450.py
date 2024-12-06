from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """
        Counts the number of students doing homework at queryTime.

        Parameters:
        startTime (List[int]): Start times of students.
        endTime (List[int]): End times of students.
        queryTime (int): The time to query.

        Returns:
        int: Number of students doing homework at queryTime.
        """
        count = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                count += 1
        return count
