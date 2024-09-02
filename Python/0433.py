from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        bank_set = set(bank)
        queue = deque([(startGene, 0)])  # (current_gene, mutation_steps)
        visited = set()
        visited.add(startGene)
        
        while queue:
            current_gene, steps = queue.popleft()
            
            if current_gene == endGene:
                return steps
            
            # Generate all possible mutations
            for i in range(len(current_gene)):
                for char in 'ACGT':
                    if char != current_gene[i]:
                        new_gene = current_gene[:i] + char + current_gene[i+1:]
                        if new_gene in bank_set and new_gene not in visited:
                            visited.add(new_gene)
                            queue.append((new_gene, steps + 1))
        
        return -1