from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Step 1: Add building 1 with height 0
        restrictions = restrictions.copy()
        restrictions.append([1, 0])

        # Step 2: Sort restrictions by building id
        restrictions.sort(key=lambda x: x[0])

        # Step 3: Add building n if not present
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        # Re-sort after adding building n
        restrictions.sort(key=lambda x: x[0])

        # Step 4: Left to right pass
        for i in range(1, len(restrictions)):
            prev_id, prev_height = restrictions[i - 1]
            current_id, current_height = restrictions[i]
            distance = current_id - prev_id
            # The current height cannot exceed previous height + distance
            max_allowed = prev_height + distance
            if current_height > max_allowed:
                restrictions[i][1] = max_allowed

        # Step 5: Right to left pass
        for i in range(len(restrictions) - 2, -1, -1):
            next_id, next_height = restrictions[i + 1]
            current_id, current_height = restrictions[i]
            distance = next_id - current_id
            # The current height cannot exceed next height + distance
            max_allowed = next_height + distance
            if restrictions[i][1] > max_allowed:
                restrictions[i][1] = max_allowed

        # Step 6: Iterate through consecutive pairs to find maximum height
        max_height = 0
        for i in range(1, len(restrictions)):
            left_id, left_height = restrictions[i - 1]
            right_id, right_height = restrictions[i]
            distance = right_id - left_id
            # Maximum height between left and right
            possible_max = (left_height + right_height + distance) // 2
            max_height = max(max_height, possible_max)

        return max_height
