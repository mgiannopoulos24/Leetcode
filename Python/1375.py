class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flipped = 0
        count = 0
        for i, flip in enumerate(flips, 1):  # 1-indexed (so enumerate starts at 1)
            max_flipped = max(max_flipped, flip)
            if max_flipped == i:
                count += 1
        return count
