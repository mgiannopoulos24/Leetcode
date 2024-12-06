class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: Calculate the number of trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n-1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        # Step 2: Count the number of swaps needed
        swaps = 0
        for i in range(n):
            required_zeros = n - i - 1
            found = False
            # Try to find a row with enough trailing zeros in the range from i to the end
            for j in range(i, n):
                if trailing_zeros[j] >= required_zeros:
                    # Found a valid row, now move it to position i
                    found = True
                    # Move this row to the i-th position by swapping adjacent rows
                    for k in range(j, i, -1):
                        trailing_zeros[k], trailing_zeros[k - 1] = trailing_zeros[k - 1], trailing_zeros[k]
                        swaps += 1
                    break
            # If we didn't find any valid row, return -1
            if not found:
                return -1
        
        return swaps
