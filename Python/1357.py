class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        # Store n (frequency of discount), discount percentage, and product-price map
        self.n = n
        self.discount = discount
        self.product_price_map = {product: price for product, price in zip(products, prices)}
        self.customer_count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        # Increment the customer count
        self.customer_count += 1
        
        # Calculate the total bill for the current customer
        total_bill = 0
        for prod, amt in zip(product, amount):
            total_bill += self.product_price_map[prod] * amt
        
        # If this customer is the nth customer, apply the discount
        if self.customer_count % self.n == 0:
            total_bill *= (100 - self.discount) / 100.0
        
        return total_bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)