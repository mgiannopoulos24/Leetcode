class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)  # Convert to a list to allow modifications

        # Handle hours (hh)
        if time[0] == '?':
            if time[1] == '?' or '0' <= time[1] <= '3':
                time[0] = '2'  # Maximize to 2 if second digit allows
            else:
                time[0] = '1'  # Otherwise, maximize to 1
        if time[1] == '?':
            time[1] = '3' if time[0] == '2' else '9'  # Maximize based on first digit

        # Handle minutes (mm)
        if time[3] == '?':
            time[3] = '5'  # Maximize first minute digit
        if time[4] == '?':
            time[4] = '9'  # Maximize second minute digit

        return ''.join(time)  # Join list back to string
