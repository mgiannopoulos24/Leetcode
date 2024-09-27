class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_trailing_zeroes(x: int) -> int:
            count = 0
            power_of_5 = 5
            while x >= power_of_5:
                count += x // power_of_5
                power_of_5 *= 5
            return count
        
        def find_first_x_with_zeroes(target: int) -> int:
            low, high = 0, 5 * (target + 1)
            while low < high:
                mid = (low + high) // 2
                if count_trailing_zeroes(mid) < target:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        first_x_with_k = find_first_x_with_zeroes(k)
        first_x_with_k_plus_1 = find_first_x_with_zeroes(k + 1)
        
        if count_trailing_zeroes(first_x_with_k) != k:
            return 0
        
        return first_x_with_k_plus_1 - first_x_with_k