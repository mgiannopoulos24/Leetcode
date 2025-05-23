class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        left_sum = right_sum = 0
        left_q = right_q = 0
        
        for i in range(half):
            ch = num[i]
            if ch == '?':
                left_q += 1
            else:
                left_sum += int(ch)
                
        for i in range(half, n):
            ch = num[i]
            if ch == '?':
                right_q += 1
            else:
                right_sum += int(ch)
        
        diff = (left_sum - right_sum) + (left_q - right_q) * 4.5
        return abs(diff) > 1e-9  # Not equal to zero