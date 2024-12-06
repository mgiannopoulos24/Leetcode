from functools import lru_cache

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # Prerequisites mask array for each course
        prereq = [0] * n
        
        # Build the prerequisite bitmask for each course
        for u, v in relations:
            prereq[v - 1] |= (1 << (u - 1))

        # dp memoization
        @lru_cache(None)
        def dp(mask):
            if mask == (1 << n) - 1:
                return 0  # All courses are completed
            
            # Find all the courses that can be taken in the current state
            available = []
            for i in range(n):
                if (mask & (1 << i)) == 0 and (mask & prereq[i]) == prereq[i]:
                    available.append(i)
            
            # Try to take up to `k` available courses
            if len(available) <= k:
                # We can take all available courses
                new_mask = mask
                for course in available:
                    new_mask |= (1 << course)
                return 1 + dp(new_mask)
            else:
                # Try all combinations of `k` available courses
                best = float('inf')
                def combine(available, k, mask, idx, count, new_mask):
                    nonlocal best
                    if count == k:
                        best = min(best, 1 + dp(new_mask))
                        return
                    if idx >= len(available):
                        return
                    # Take this course
                    combine(available, k, mask, idx + 1, count + 1, new_mask | (1 << available[idx]))
                    # Don't take this course
                    combine(available, k, mask, idx + 1, count, new_mask)

                combine(available, k, mask, 0, 0, mask)
                return best

        # Start from empty bitmask (no courses taken)
        return dp(0)
