class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        perm = []
        low, high = 0, n
        
        # Traverse the string s
        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else:  # char == 'D'
                perm.append(high)
                high -= 1
        
        # Append the last number
        perm.append(low)  # at this point low == high
        
        return perm
