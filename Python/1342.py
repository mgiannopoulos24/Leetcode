class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:  # Even
                num //= 2
            else:  # Odd
                num -= 1
            steps += 1
        return steps
