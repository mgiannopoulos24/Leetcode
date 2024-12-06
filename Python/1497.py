class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k  # Array to store counts of remainders
        
        # Count occurrences of each remainder
        for num in arr:
            remainder = num % k
            # Handling negative remainders by making sure they are positive
            remainder_count[remainder] += 1
        
        # Check if pairs can be formed
        for i in range(1, k):  # Start from 1 to avoid checking remainder 0 here
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        # Special case: the count of remainder 0 should be even (pairs among themselves)
        return remainder_count[0] % 2 == 0
