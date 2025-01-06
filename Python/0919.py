# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque()
        self.queue.append(root)
        
        # Process the queue to find all nodes with at least one empty child
        while self.queue:
            node = self.queue[0]
            if node.left and node.right:
                self.queue.popleft()
                self.queue.append(node.left)
                self.queue.append(node.right)
            else:
                if node.left:
                    self.queue.append(node.left)
                break

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        parent = self.queue[0]
        
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.queue.popleft()
        
        self.queue.append(new_node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()