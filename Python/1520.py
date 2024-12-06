from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # Step 1: Record the first and last occurrence of each character
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        # Step 2: Find all valid substrings
        substrings = []
        for c in first:
            start = first[c]
            end = last[c]
            i = start
            valid = True
            while i <= end:
                current_char = s[i]
                if first[current_char] < start:
                    # Extend the start if needed
                    start = first[current_char]
                    # Reset the scanning
                    i = start
                    end = last[current_char]
                    continue
                if last[current_char] > end:
                    # Extend the end if needed
                    end = last[current_char]
                    # Reset the scanning
                    i = start
                    continue
                i += 1
            # After expansion, check if the substring is valid
            # i.e., it contains all occurrences of its characters
            is_valid = True
            for j in range(start, end + 1):
                c_j = s[j]
                if first[c_j] < start or last[c_j] > end:
                    is_valid = False
                    break
            if is_valid:
                substrings.append((start, end))

        # Step 3: Sort the substrings by end index, then by length
        substrings.sort(key=lambda x: (x[1], x[0]))

        # Step 4: Select non-overlapping substrings
        result = []
        last_end = -1
        for start, end in substrings:
            if start > last_end:
                result.append(s[start:end+1])
                last_end = end

        return result
