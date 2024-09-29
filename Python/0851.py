from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        
        # Step 1: Build a graph where an edge goes from 'richer' to 'poorer'
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)  # Person v is poorer than u
        
        # Step 2: Memoization array to store the quietest person for each node
        answer = [-1] * n
        
        # Step 3: DFS function to find the quietest person for a given person
        def dfs(person: int) -> int:
            if answer[person] != -1:
                return answer[person]
            
            # Start by assuming the quietest person is the person itself
            answer[person] = person
            
            # Explore all people richer than this person
            for richer_person in graph[person]:
                candidate = dfs(richer_person)
                if quiet[candidate] < quiet[answer[person]]:
                    answer[person] = candidate
            
            return answer[person]
        
        # Step 4: Run DFS for each person
        for i in range(n):
            dfs(i)
        
        return answer
