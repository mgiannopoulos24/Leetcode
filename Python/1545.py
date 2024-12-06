class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: S1 is "0"
        if n == 1:
            return "0"
        
        # Length of Sn is 2^n - 1
        mid = (1 << (n - 1))  # This is 2^(n-1), which gives us the middle index
        
        if k == mid:
            return "1"
        elif k < mid:
            # Recurse on the left half (S[n-1])
            return self.findKthBit(n - 1, k)
        else:
            # Recurse on the right half (reverse(invert(S[n-1])))
            # This corresponds to (2^n - k) in S[n-1], with inversion
            return "1" if self.findKthBit(n - 1, mid - (k - mid)) == "0" else "0"
