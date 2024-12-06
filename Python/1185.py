import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Create a date object from the given day, month, and year
        date = datetime.date(year, month, day)
        
        # List of days of the week, where Monday is at index 0 and Sunday is at index 6
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        # Use weekday() to get the index of the day (0 = Monday, 6 = Sunday)
        return days_of_week[date.weekday()]
