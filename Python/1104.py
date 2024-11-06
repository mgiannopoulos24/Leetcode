class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        while label >= 1:
            path.append(label)
            level = label.bit_length() - 1
            label = ((1 << level) + (1 << (level + 1)) - 1 - label) // 2
        return path[::-1]
