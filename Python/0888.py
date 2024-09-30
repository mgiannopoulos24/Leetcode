class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        
        # Calculate the target sum each should have after swap
        target = (sumA + sumB) // 2
        
        # Calculate the difference
        diff = sumA - target
        
        # Use a set for efficient lookup
        aliceSet = set(aliceSizes)
        
        # Iterate through Bob's candies
        for b in bobSizes:
            # Calculate the required candy from Alice's set
            a = b + diff
            if a in aliceSet:
                return [a, b]

        return []  # Just a placeholder, as the problem guarantees there is at least one valid answer
