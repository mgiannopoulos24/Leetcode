class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        # Iterate over the target string
        for i in range(len(target)):
            # If the current character differs from the previous one, we need a flip
            if i == 0:  # First character is special, compare with '0'
                if target[i] != '0':
                    flips += 1
            else:
                if target[i] != target[i - 1]:
                    flips += 1
        
        return flips
