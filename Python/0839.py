class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(s1: str, s2: str) -> bool:
            # Check if two strings are similar
            diff = 0
            for a, b in zip(s1, s2):
                if a != b:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 2 or diff == 0
        
        def dfs(node: str):
            # Perform DFS to mark all similar nodes
            stack = [node]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
        
        # Create the graph
        graph = {s: [] for s in strs}
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if isSimilar(strs[i], strs[j]):
                    graph[strs[i]].append(strs[j])
                    graph[strs[j]].append(strs[i])
        
        # Find the number of connected components
        visited = {s: False for s in strs}
        num_groups = 0
        for s in strs:
            if not visited[s]:
                visited[s] = True
                dfs(s)
                num_groups += 1
        
        return num_groups
