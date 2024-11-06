class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Increment depth and assign based on whether depth is even or odd
                depth += 1
                result.append(depth % 2)
            else:
                # Assign based on current depth and then decrement depth
                result.append(depth % 2)
                depth -= 1
        
        return result
