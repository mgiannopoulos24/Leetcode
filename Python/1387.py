class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Dictionary to cache power values for each number
        power_cache = {}

        # Helper function to calculate the power of a number
        def get_power(x):
            if x == 1:
                return 0
            if x in power_cache:
                return power_cache[x]
            if x % 2 == 0:
                power_cache[x] = 1 + get_power(x // 2)
            else:
                power_cache[x] = 1 + get_power(3 * x + 1)
            return power_cache[x]

        # Create a list of numbers with their power values
        numbers_with_power = []
        for num in range(lo, hi + 1):
            power = get_power(num)
            numbers_with_power.append((power, num))

        # Sort by power first, and by the number itself if powers are the same
        numbers_with_power.sort()

        # Return the k-th element (0-indexed, so return k-1)
        return numbers_with_power[k - 1][1]
