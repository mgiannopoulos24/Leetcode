from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Parse the date strings into datetime.date objects
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        
        # Compute the difference in days and return the absolute value
        return abs((d2 - d1).days)
