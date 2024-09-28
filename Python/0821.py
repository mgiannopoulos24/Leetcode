class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        distances = [float('inf')] * n
        
        # Forward pass
        last_occurrence = float('-inf')
        for i in range(n):
            if s[i] == c:
                last_occurrence = i
            distances[i] = min(distances[i], abs(i - last_occurrence))
        
        # Backward pass
        last_occurrence = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last_occurrence = i
            distances[i] = min(distances[i], abs(i - last_occurrence))
        
        return distances
