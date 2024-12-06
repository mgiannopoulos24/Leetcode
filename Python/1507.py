class Solution:
    def reformatDate(self, date: str) -> str:
        # Dictionary to map month abbreviations to their corresponding number
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        
        # Split the date string into day, month, and year
        day, month, year = date.split()
        
        # Remove the suffix ('st', 'nd', 'rd', 'th') from the day and convert to two digits
        day = day[:-2].zfill(2)
        
        # Format the final date as YYYY-MM-DD
        return f"{year}-{month_map[month]}-{day}"
