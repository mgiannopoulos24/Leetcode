from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment: str) -> bool:
            # Check if the segment is valid:
            # 1. It should not be empty
            # 2. It should not have leading zeros
            # 3. It should be between 0 and 255
            return (len(segment) > 0 and len(segment) <= 3
                    and (segment[0] != '0' or len(segment) == 1)
                    and 0 <= int(segment) <= 255)
        
        def backtrack(start: int, path: List[str]):
            # If we have 4 segments and we have processed the entire string
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            
            # Try to create segments of length 1, 2, or 3
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if is_valid(segment):
                        path.append(segment)
                        backtrack(start + length, path)
                        path.pop()
        
        result = []
        backtrack(0, [])
        return result