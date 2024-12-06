class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # Step 1: Create a prefix sum matrix
        prefixSum = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefixSum[i][j] = mat[i-1][j-1] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
        
        # Step 2: Helper function to calculate the sum of a square (i, j) with size "side"
        def getSquareSum(x1, y1, side):
            x2, y2 = x1 + side - 1, y1 + side - 1
            return (prefixSum[x2+1][y2+1] 
                    - prefixSum[x1][y2+1] 
                    - prefixSum[x2+1][y1] 
                    + prefixSum[x1][y1])

        # Step 3: Binary search for the maximum side length
        low, high = 0, min(m, n)
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            found = False
            
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if getSquareSum(i, j, mid) <= threshold:
                        found = True
                        break
                if found:
                    break
            
            if found:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result
