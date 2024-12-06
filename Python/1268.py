class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Step 1: Sort the products lexicographically
        products.sort()
        
        result = []
        prefix = ""
        
        # Step 2: For each character in searchWord, form the prefix and search
        for char in searchWord:
            prefix += char
            # Filter products that start with the current prefix
            suggestions = []
            for product in products:
                if product.startswith(prefix):
                    suggestions.append(product)
                # Since products are sorted, we can stop after finding three matches
                if len(suggestions) == 3:
                    break
            result.append(suggestions)
        
        return result
