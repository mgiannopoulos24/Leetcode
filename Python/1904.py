class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        # Helper function to convert time to minutes since midnight
        def time_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes

        # Helper function to round up to the next 15-minute mark
        def round_up_to_next_15(minutes: int) -> int:
            return ((minutes + 14) // 15) * 15

        # Helper function to round down to the previous 15-minute mark
        def round_down_to_previous_15(minutes: int) -> int:
            return (minutes // 15) * 15

        # Convert loginTime and logoutTime to total minutes since midnight
        login_minutes = time_to_minutes(loginTime)
        logout_minutes = time_to_minutes(logoutTime)

        # Handle the case where logoutTime is earlier than loginTime (spanning midnight)
        if logout_minutes < login_minutes:
            logout_minutes += 1440  # Add 24 hours worth of minutes

        # Round loginTime up and logoutTime down
        rounded_login = round_up_to_next_15(login_minutes)
        rounded_logout = round_down_to_previous_15(logout_minutes)

        # Calculate the number of full rounds
        if rounded_login >= rounded_logout:
            return 0
        return (rounded_logout - rounded_login) // 15