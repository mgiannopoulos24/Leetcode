from collections import defaultdict
from math import isqrt
from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    rootX, rootY = rootY, rootX
                parent[rootX] = rootY
                size[rootY] += size[rootX]
        
        def prime_factors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            for i in range(3, isqrt(n) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 2:
                factors.add(n)
            return factors
        
        # Union-Find Initialization
        parent = {}
        size = {}
        for num in nums:
            parent[num] = num
            size[num] = 1
        
        # Map from factor to the first number having this factor
        factor_map = defaultdict(int)
        
        for num in nums:
            factors = prime_factors(num)
            for factor in factors:
                if factor in factor_map:
                    union(num, factor_map[factor])
                factor_map[factor] = num
        
        # Calculate the size of each component
        component_size = defaultdict(int)
        for num in nums:
            root = find(num)
            component_size[root] += 1
        
        # The largest component size
        return max(component_size.values())
