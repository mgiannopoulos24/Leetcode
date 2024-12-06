from collections import defaultdict
import bisect

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        
        # Store positions of each element for efficient frequency queries
        self.pos = defaultdict(list)
        for i, num in enumerate(arr):
            self.pos[num].append(i)
        
        # Build the segment tree
        self.seg_tree = [None] * (4 * self.n)
        self.build(0, 0, self.n - 1)
    
    def build(self, node, l, r):
        if l == r:
            self.seg_tree[node] = self.arr[l]
        else:
            mid = (l + r) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self.build(left_child, l, mid)
            self.build(right_child, mid + 1, r)
            
            # Get the majority candidate by merging left and right
            left_major = self.seg_tree[left_child]
            right_major = self.seg_tree[right_child]
            
            if left_major == right_major:
                self.seg_tree[node] = left_major
            else:
                # Count occurrences of both candidates
                left_count = self.count_in_range(left_major, l, r)
                right_count = self.count_in_range(right_major, l, r)
                
                # Choose the candidate that occurs more
                if left_count > right_count:
                    self.seg_tree[node] = left_major
                else:
                    self.seg_tree[node] = right_major
    
    def count_in_range(self, num, l, r):
        """Count occurrences of 'num' in the range [l, r] using binary search."""
        if num not in self.pos:
            return 0
        positions = self.pos[num]
        # Find the count of positions in the range [l, r]
        left_idx = bisect.bisect_left(positions, l)
        right_idx = bisect.bisect_right(positions, r)
        return right_idx - left_idx
    
    def query(self, left: int, right: int, threshold: int) -> int:
        # Get candidate majority element from segment tree
        candidate = self.query_seg_tree(0, 0, self.n - 1, left, right)
        
        # Verify if this candidate appears at least 'threshold' times
        if self.count_in_range(candidate, left, right) >= threshold:
            return candidate
        return -1
    
    def query_seg_tree(self, node, l, r, left, right):
        if l > right or r < left:
            return -1  # Out of bounds, return invalid candidate
        
        if l >= left and r <= right:
            return self.seg_tree[node]
        
        mid = (l + r) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        left_major = self.query_seg_tree(left_child, l, mid, left, right)
        right_major = self.query_seg_tree(right_child, mid + 1, r, left, right)
        
        if left_major == -1:
            return right_major
        if right_major == -1:
            return left_major
        
        if left_major == right_major:
            return left_major
        
        # Determine which of the two is the better candidate
        left_count = self.count_in_range(left_major, left, right)
        right_count = self.count_in_range(right_major, left, right)
        
        if left_count > right_count:
            return left_major
        else:
            return right_major



# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)