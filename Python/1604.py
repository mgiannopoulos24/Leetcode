from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # Helper function to convert "HH:MM" to minutes since the start of the day
        def timeToMinutes(time_str):
            hours, minutes = map(int, time_str.split(":"))
            return hours * 60 + minutes
        
        # Dictionary to group key usage times by employee
        name_to_times = defaultdict(list)
        
        # Populate the dictionary with key usage times for each employee
        for name, time in zip(keyName, keyTime):
            name_to_times[name].append(timeToMinutes(time))
        
        # List to store names of employees who triggered an alert
        alert_names = []
        
        # Check each employee's key usage times
        for name, times in name_to_times.items():
            times.sort()  # Sort the times for this employee
            
            # Check for any 3 consecutive times that are within 60 minutes
            for i in range(len(times) - 2):
                # If the difference between the third and first is <= 60 minutes, trigger an alert
                if times[i + 2] - times[i] <= 60:
                    alert_names.append(name)
                    break  # No need to check further for this employee
        
        # Return the sorted list of alert names
        return sorted(alert_names)
