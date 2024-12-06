class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        current = 0
        
        # Iterate through the stream of integers from 1 to n
        for i in range(1, n + 1):
            if current >= len(target):
                break
            if target[current] == i:
                # Match found, perform a "Push" operation
                operations.append("Push")
                current += 1
            else:
                # Skip this number, perform "Push" and "Pop"
                operations.append("Push")
                operations.append("Pop")
        
        return operations
