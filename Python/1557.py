class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Create an array to store the in-degree of each node
        in_degree = [0] * n
        
        # Step 2: Traverse the edges and increment the in-degree of the destination node
        for edge in edges:
            from_node, to_node = edge
            in_degree[to_node] += 1
        
        # Step 3: Collect all nodes with an in-degree of 0 (no incoming edges)
        result = [node for node in range(n) if in_degree[node] == 0]
        
        return result
