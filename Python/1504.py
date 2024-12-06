class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        result = 0

        # Precompute heights of consecutive 1s in each column
        heights = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[i][j] = heights[i-1][j] + 1 if i > 0 else 1
        
        # For each row, count the number of submatrices ending at each position
        for i in range(m):
            stack = []
            count = [0] * n
            for j in range(n):
                h = heights[i][j]
                while stack and heights[i][stack[-1]] >= h:
                    stack.pop()
                
                if stack:
                    count[j] = count[stack[-1]] + h * (j - stack[-1])
                else:
                    count[j] = h * (j + 1)
                
                result += count[j]
                stack.append(j)

        return result
