from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # Step 1: Create sets for unique food items and dictionary for table orders
        food_items = set()
        table_orders = defaultdict(lambda: defaultdict(int))
        
        # Step 2: Populate the data structures
        for customer_name, table_number, food_item in orders:
            food_items.add(food_item)
            table_orders[table_number][food_item] += 1
        
        # Step 3: Sort the food items alphabetically
        sorted_food_items = sorted(food_items)
        
        # Step 4: Sort the table numbers numerically
        sorted_tables = sorted(table_orders.keys(), key=lambda x: int(x))
        
        # Step 5: Build the result table
        result = []
        
        # Add the header
        header = ["Table"] + sorted_food_items
        result.append(header)
        
        # Add each table's data row
        for table in sorted_tables:
            row = [table]  # Start the row with the table number
            for food in sorted_food_items:
                row.append(str(table_orders[table].get(food, 0)))  # Add food item count or 0 if not ordered
            result.append(row)
        
        return result