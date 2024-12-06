class ProductOfNumbers:

    def __init__(self):
        # Prefix product array, starting with a base of 1
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # If we encounter a zero, reset the prefix products
            self.prefix_products = [1]
        else:
            # Add the product of the current number with the last prefix product
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is larger than the number of available products after the last reset (due to a 0), return 0
        if k >= len(self.prefix_products):
            return 0
        # Otherwise, calculate the product using the prefix product division
        return self.prefix_products[-1] // self.prefix_products[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)