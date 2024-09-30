# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Create a parent mapping and find the target node
        def dfs(node: TreeNode, parent: Optional[TreeNode]) -> None:
            if node:
                parent_map[node] = parent
                dfs(node.left, node)
                dfs(node.right, node)
        
        parent_map = {}
        dfs(root, None)
        
        # Step 2: Use BFS to find nodes at distance k from the target node
        result = []
        queue = deque([(target, 0)])  # (current_node, current_distance)
        visited = set([target])
        
        while queue:
            node, dist = queue.popleft()
            
            if dist == k:
                result.append(node.val)
            
            for neighbor in (node.left, node.right, parent_map.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return result