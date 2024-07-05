class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev_term = "1"
        
        for _ in range(2, n + 1):
            current_term = []
            i = 0
            while i < len(prev_term):
                count = 1
                while i + 1 < len(prev_term) and prev_term[i] == prev_term[i + 1]:
                    count += 1
                    i += 1
                current_term.append(str(count))
                current_term.append(prev_term[i])
                i += 1
            prev_term = ''.join(current_term)
        
        return prev_term
