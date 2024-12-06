class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        
        # Iterate over each possible starting point for the pattern
        for i in range(n - m * k + 1):  # Ensure we have enough room for m*k elements
            # Check if the pattern starting at i repeats k times
            pattern = arr[i:i + m]
            count = 1
            
            for j in range(i + m, n, m):
                if arr[j:j + m] == pattern:
                    count += 1
                else:
                    break
                
                if count >= k:
                    return True
        
        return False
