from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def generate_array(x):
            if x == 1:
                return [1]
            else:
                # Generate the beautiful arrays for the smaller problem
                odd = generate_array((x + 1) // 2)
                even = generate_array(x // 2)
                
                # Combine the results
                return [2 * num - 1 for num in odd] + [2 * num for num in even]
        
        return generate_array(n)
