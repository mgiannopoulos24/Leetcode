from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(k: int):
            # Reverse the first k elements
            arr[:k] = reversed(arr[:k])
            flips.append(k)

        n = len(arr)
        flips = []

        for i in range(n):
            # Find the position of the target value i+1
            target = n - i
            target_index = arr.index(target)

            if target_index == n - i - 1:
                # The target is already in the correct position
                continue

            if target_index != 0:
                # Flip to move the target to the front
                flip(target_index + 1)

            # Flip to move the target to its final position
            flip(n - i)

        return flips
