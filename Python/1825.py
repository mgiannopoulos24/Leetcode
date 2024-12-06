from typing import List
from collections import deque

class FenwickTree:
    def __init__(self, size):
        self.N = size + 2  # 1-based indexing
        self.tree = [0] * (self.N)
    
    def add(self, index, delta):
        while index < self.N:
            self.tree[index] += delta
            index += index & -index
    
    def sum(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res
    
    def find_kth(self, k):
        idx = 0
        bit_mask = 1 << 17  # Since size <= 10^5, 2^17 > 10^5
        while bit_mask != 0:
            t_idx = idx + bit_mask
            if t_idx < self.N and self.tree[t_idx] < k:
                idx = t_idx
                k -= self.tree[t_idx]
            bit_mask >>= 1
        return idx + 1  # 1-based indexing

class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue = deque()
        self.max_num = 100001  # as per constraints, num <= 10^5
        self.count_tree = FenwickTree(self.max_num)
        self.sum_tree = FenwickTree(self.max_num)
        self.total_sum = 0

    def addElement(self, num: int) -> None:
        self.queue.append(num)
        self.count_tree.add(num, 1)
        self.sum_tree.add(num, num)
        self.total_sum += num

        if len(self.queue) > self.m:
            old = self.queue.popleft()
            self.count_tree.add(old, -1)
            self.sum_tree.add(old, -old)
            self.total_sum -= old

    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m:
            return -1
        
        k = self.k
        m = self.m
        # Sum of smallest k elements
        smallest_sum = self.get_smallest_sum(k)
        # Sum of largest k elements
        largest_sum = self.get_largest_sum(k)
        # Sum of middle elements
        middle_sum = self.total_sum - smallest_sum - largest_sum
        return middle_sum // (m - 2 * k)
    
    def get_smallest_sum(self, k):
        # Find the k-th smallest number
        kth = self.count_tree.find_kth(k)
        # Sum of all numbers less than kth
        sum_less = self.sum_tree.sum(kth - 1)
        # Count of numbers less than kth
        cnt_less = self.count_tree.sum(kth - 1)
        # Number of times kth appears
        cnt_kth = self.count_tree.sum(kth) - self.count_tree.sum(kth - 1)
        # Number of kth needed
        need = k - cnt_less
        sum_kth = kth * min(need, cnt_kth)
        return sum_less + sum_kth
    
    def get_largest_sum(self, k):
        # Total count
        total_count = self.count_tree.sum(self.max_num -1)
        # Find the (total_count - k +1)-th smallest number, which is the k-th largest
        kth = self.count_tree.find_kth(total_count - k +1)
        # Sum of all numbers less than kth
        sum_less = self.sum_tree.sum(kth -1)
        # Count of numbers less than kth
        cnt_less = self.count_tree.sum(kth -1)
        # Count of kth
        cnt_kth = self.count_tree.sum(kth) - self.count_tree.sum(kth -1)
        # Number of kth needed
        need = k - (total_count - self.count_tree.sum(kth))
        need = k - (self.count_tree.sum(self.max_num -1) - self.count_tree.sum(kth))
        need = min(need, cnt_kth)
        sum_kth = kth * need
        return self.sum_tree.sum(self.max_num -1) - (sum_less + (kth * (cnt_kth - need)))


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()