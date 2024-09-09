from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # Initialize a counter for seniors
        senior_count = 0
        
        # Iterate over each passenger's details
        for detail in details:
            # Extract age from the 12th and 13th characters (0-indexed positions 11 and 12)
            age_str = detail[11:13]
            # Convert the age string to an integer
            age = int(age_str)
            # Check if the age is greater than 60
            if age > 60:
                senior_count += 1
        
        return senior_count
