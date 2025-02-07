class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # Preprocessing
        # 1. List of all candle indices
        candles = [i for i, char in enumerate(s) if char == '|']
        # 2. Prefix sum of plates
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if s[i] == '*' else 0)
        # 3. Nearest left candle for each index
        left_candle = [-1] * n
        last_candle = -1
        for i in range(n):
            if s[i] == '|':
                last_candle = i
            left_candle[i] = last_candle
        # 4. Nearest right candle for each index
        right_candle = [n] * n
        last_candle = n
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                last_candle = i
            right_candle[i] = last_candle
        
        # Processing queries
        result = []
        for left, right in queries:
            # Find the leftmost candle in [left, right]
            l = right_candle[left]
            # Find the rightmost candle in [left, right]
            r = left_candle[right]
            if l == n or r == -1 or l > r:
                result.append(0)
            else:
                # Number of plates between l and r
                result.append(prefix[r+1] - prefix[l+1])
        return result