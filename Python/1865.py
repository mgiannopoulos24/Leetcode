class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        from collections import Counter
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.counter2[self.nums2[index]] -= 1
        if self.counter2[self.nums2[index]] == 0:
            del self.counter2[self.nums2[index]]
        self.nums2[index] += val
        self.counter2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        result = 0
        for num1 in self.nums1:
            complement = tot - num1
            if complement in self.counter2:
                result += self.counter2[complement]
        return result

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
