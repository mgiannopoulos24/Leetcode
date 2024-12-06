from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # Step 1: Build the adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Result array to store the count of nodes with the same label
        result = [0] * n
        
        # Step 3: Perform DFS to compute the result
        def dfs(node: int, parent: int) -> List[int]:
            # Create a count array for the current subtree (26 letters in total)
            count = [0] * 26
            # Get the current node's label and its corresponding index
            label_index = ord(labels[node]) - ord('a')
            
            # This node contributes 1 to its own label's count
            count[label_index] = 1
            
            # Visit all the children
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                # Get the count of labels from the child's subtree
                child_count = dfs(neighbor, node)
                
                # Add the child's label counts to the current node's counts
                for i in range(26):
                    count[i] += child_count[i]
            
            # Set the result for the current node as the count of its own label in the subtree
            result[node] = count[label_index]
            return count
        
        # Start DFS from node 0 (root) and assume it has no parent (i.e., -1)
        dfs(0, -1)
        
        return result
