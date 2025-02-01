class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num):
            from collections import defaultdict
            count = defaultdict(int)
            for digit in str(num):
                count[int(digit)] += 1
            for digit, cnt in count.items():
                if cnt != digit:
                    return False
            return True
        
        current = n + 1
        while True:
            if is_balanced(current):
                return current
            current += 1