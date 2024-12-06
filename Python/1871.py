class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] != '0':
            return False

        reachable = [False] * n
        reachable[0] = True
        max_reach = 0

        for i in range(1, n):
            if i >= minJump:
                max_reach += reachable[i - minJump]
            if i > maxJump:
                max_reach -= reachable[i - maxJump - 1]

            reachable[i] = max_reach > 0 and s[i] == '0'

        return reachable[-1]
