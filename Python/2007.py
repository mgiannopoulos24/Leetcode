class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        freq = {}
        original = []

        # Count the frequency of each number in changed
        for num in changed:
            freq[num] = freq.get(num, 0) + 1

        for num in changed:
            if freq[num] == 0:  # Already used in a pair
                continue

            # Check if double of current num exists
            if freq.get(num * 2, 0) == 0:
                return []

            # Use this number and its double
            original.append(num)
            freq[num] -= 1
            freq[num * 2] -= 1

        return original
