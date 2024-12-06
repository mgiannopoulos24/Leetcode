from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # Step 1: Union-Find to determine connected components
        n = len(source)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        # Apply unions for each allowed swap
        for a, b in allowedSwaps:
            union(a, b)
        
        # Group all indices by their connected component
        components = defaultdict(list)
        for i in range(n):
            root = find(i)
            components[root].append(i)
        
        # Step 2: Calculate the minimum Hamming distance
        min_hamming_distance = 0
        for indices in components.values():
            # Collect counts of elements in source and target for the current component
            source_count = Counter(source[i] for i in indices)
            target_count = Counter(target[i] for i in indices)
            
            # Calculate mismatches within this component
            # Total mismatches is the count of unmatched elements
            for elem, count in target_count.items():
                # Reduce the mismatches by the number of common elements in source and target
                min_hamming_distance += max(0, count - source_count[elem])
        
        return min_hamming_distance
