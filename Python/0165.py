class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the versions into lists of integers
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        # Get the maximum length of the two version lists
        max_len = max(len(v1), len(v2))
        
        # Compare corresponding elements
        for i in range(max_len):
            # Get the current revision, default to 0 if index is out of range
            num1 = v1[i] if i < len(v1) else 0
            num2 = v2[i] if i < len(v2) else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        return 0
