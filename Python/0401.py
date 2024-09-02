from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        results = []
        
        # Iterate over all possible hours and minutes
        for h in range(12):
            for m in range(60):
                # Count the number of bits set to 1 in hour and minute
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # Format the time properly (no leading zero for hour, always two digits for minute)
                    results.append(f"{h}:{m:02d}")
        
        return results
