class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        result = [[0] * n for _ in range(2)]  # 2xN matrix initialized to 0
        
        # Step 1: Traverse the colsum array and fill the matrix
        for i in range(n):
            if colsum[i] == 2:
                if upper > 0 and lower > 0:
                    result[0][i] = 1
                    result[1][i] = 1
                    upper -= 1
                    lower -= 1
                else:
                    return []  # Impossible to allocate both 1s when upper or lower is 0
            elif colsum[i] == 1:
                if upper > lower and upper > 0:
                    result[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    result[1][i] = 1
                    lower -= 1
                else:
                    return []  # Impossible to allocate a 1 when both upper and lower are exhausted
        
        # Step 2: Ensure both upper and lower are now zero
        if upper == 0 and lower == 0:
            return result
        else:
            return []  # If we have remaining upper or lower, it's impossible to create a valid matrix
