from collections import deque

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Step 1: Find the in-degree of each node
        in_degree = [0] * n
        
        for i in range(n):
            if leftChild[i] != -1:
                in_degree[leftChild[i]] += 1
            if rightChild[i] != -1:
                in_degree[rightChild[i]] += 1
        
        # Step 2: Find the root (node with in-degree 0)
        root = -1
        for i in range(n):
            if in_degree[i] == 0:
                if root == -1:
                    root = i
                else:
                    # More than one root (invalid tree)
                    return False
        
        # If there's no root at all, return False
        if root == -1:
            return False
        
        # Step 3: Check for cycles and whether all nodes are reachable using BFS/DFS
        visited = [False] * n
        queue = deque([root])
        visited[root] = True
        visited_count = 1
        
        while queue:
            node = queue.popleft()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if visited[child]:
                        # If we visit an already visited node, there's a cycle
                        return False
                    visited[child] = True
                    queue.append(child)
                    visited_count += 1
        
        # Step 4: Ensure that all nodes were visited (tree must be connected)
        return visited_count == n
