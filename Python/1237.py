"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        # x ranges from 1 to 1000
        for x in range(1, 1001):
            # Start with y = 1000 and decrease as needed
            y = 1000
            while y >= 1:
                value = customfunction.f(x, y)
                if value == z:
                    result.append([x, y])
                    # Once we find a pair, continue with smaller y
                    y -= 1
                elif value > z:
                    # If f(x, y) is greater than z, we decrease y
                    y -= 1
                else:
                    # Since f(x, y) is monotonically increasing, we can stop searching for this x
                    break
        
        return result
