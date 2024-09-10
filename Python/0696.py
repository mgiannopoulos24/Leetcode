class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Step 1: Count lengths of consecutive groups of '0's and '1's
        groups = []
        current_char = s[0]
        current_length = 0
        
        for char in s:
            if char == current_char:
                current_length += 1
            else:
                groups.append(current_length)
                current_char = char
                current_length = 1
        # Append the last group
        groups.append(current_length)
        
        # Step 2: Calculate the number of valid substrings
        count = 0
        for i in range(1, len(groups)):
            count += min(groups[i - 1], groups[i])
        
        return count
