class Solution:
    def dayOfYear(self, date: str) -> int:
        # Parse the input date
        year, month, day = map(int, date.split('-'))
        
        # Number of days in each month for a non-leap year
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Check if the year is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29  # February has 29 days in a leap year
        
        # Calculate the day of the year
        return sum(days_in_month[:month - 1]) + day
