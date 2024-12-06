class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7

        # Helper function to calculate sum of all balls between price high and low (inclusive)
        def sum_range(high, low):
            return (high * (high + 1)) // 2 - (low * (low + 1)) // 2

        # Sort the inventory in descending order
        inventory.sort(reverse=True)
        inventory.append(0)  # Add a zero at the end to handle all items

        result = 0
        i = 0
        while orders > 0:
            if inventory[i] > inventory[i + 1]:
                # Number of balls we can sell at this price level
                count = (i + 1) * (inventory[i] - inventory[i + 1])
                if orders >= count:
                    # We can sell all the balls between inventory[i] and inventory[i + 1]
                    result += (i + 1) * sum_range(inventory[i], inventory[i + 1]) % MOD
                    orders -= count
                else:
                    # We cannot sell all, so find how many full levels we can sell
                    full, remainder = divmod(orders, i + 1)
                    result += (i + 1) * sum_range(inventory[i], inventory[i] - full) % MOD
                    result += remainder * (inventory[i] - full) % MOD
                    orders = 0
            i += 1

        return result % MOD
