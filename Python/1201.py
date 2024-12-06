from math import gcd

class Solution:
    # Function to calculate the least common multiple (LCM)
    def lcm(self, x: int, y: int) -> int:
        return x * y // gcd(x, y)
    
    # Function to count how many ugly numbers ≤ k
    def countUglyNumbers(self, k: int, a: int, b: int, c: int) -> int:
        ab = self.lcm(a, b)
        bc = self.lcm(b, c)
        ac = self.lcm(a, c)
        abc = self.lcm(a, bc)
        return (k // a) + (k // b) + (k // c) \
             - (k // ab) - (k // bc) - (k // ac) \
             + (k // abc)

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        low, high = 1, 2 * 10**9
        
        while low < high:
            mid = (low + high) // 2
            if self.countUglyNumbers(mid, a, b, c) < n:
                low = mid + 1
            else:
                high = mid
        
        return low
