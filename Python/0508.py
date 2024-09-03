# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def subtree_sum(node):
            if not node:
                return 0
            
            # Calculate the subtree sum recursively
            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)
            total_sum = node.val + left_sum + right_sum
            
            # Count the frequency of each subtree sum
            sum_count[total_sum] += 1
            
            return total_sum
        
        # Dictionary to count frequencies of sums
        sum_count = defaultdict(int)
        
        # Calculate all subtree sums starting from the root
        subtree_sum(root)
        
        # Find the maximum frequency
        max_freq = max(sum_count.values())
        
        # Collect all sums with the maximum frequency
        most_frequent_sums = [s for s, freq in sum_count.items() if freq == max_freq]
        
        return most_frequent_sums