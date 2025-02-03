from collections import defaultdict

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        tree = defaultdict(list)
        
        # Build the tree
        for i in range(n):
            if parents[i] != -1:
                tree[parents[i]].append(i)
        
        # To store the size of each subtree
        size = [1] * n
        
        # Post-order traversal to calculate subtree sizes
        def dfs(node):
            for child in tree[node]:
                dfs(child)
                size[node] += size[child]
        
        dfs(0)
        
        max_score = 0
        count = 0
        
        for i in range(n):
            # Calculate the product of the sizes of the subtrees
            product = 1
            total = 0
            for child in tree[i]:
                product *= size[child]
                total += size[child]
            # The size of the subtree above the current node
            if i != 0:
                product *= (n - total - 1)
            # Update max_score and count
            if product > max_score:
                max_score = product
                count = 1
            elif product == max_score:
                count += 1
        
        return count