class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        sum_ = 0
        n = 0
        
        while sum_ < target or (sum_ - target) % 2 != 0:
            n += 1
            sum_ += n
        
        return n
