class Solution:
    def checkRecord(self, s: str) -> bool:
        # Check for the number of absences
        absences = s.count('A')
        if absences >= 2:
            return False
        
        # Check for consecutive late days
        consecutive_late = 0
        for char in s:
            if char == 'L':
                consecutive_late += 1
                if consecutive_late >= 3:
                    return False
            else:
                consecutive_late = 0
        
        return True
