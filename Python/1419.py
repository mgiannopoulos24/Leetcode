class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # Counters for each stage of the "croak"
        c_count = r_count = o_count = a_count = k_count = 0
        max_frogs = 0
        
        for ch in croakOfFrogs:
            if ch == 'c':
                c_count += 1
                max_frogs = max(max_frogs, c_count - k_count)  # Track concurrent croaks
            elif ch == 'r':
                if c_count <= r_count:
                    return -1
                r_count += 1
            elif ch == 'o':
                if r_count <= o_count:
                    return -1
                o_count += 1
            elif ch == 'a':
                if o_count <= a_count:
                    return -1
                a_count += 1
            elif ch == 'k':
                if a_count <= k_count:
                    return -1
                k_count += 1
            else:
                return -1
        
        # At the end, all croaks should be complete, so all counters should be equal
        if c_count == r_count == o_count == a_count == k_count:
            return max_frogs
        else:
            return -1