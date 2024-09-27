class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Step 1: Create a mapping from character to its index in `order`
        order_index = {char: i for i, char in enumerate(order)}
        
        # Step 2: Count occurrences of each character in `s`
        from collections import Counter
        s_count = Counter(s)
        
        # Step 3: Build the result based on the custom order
        result = []
        
        # Append characters that are in the `order` string, in the order specified
        for char in order:
            if char in s_count:
                result.append(char * s_count[char])
        
        # Append remaining characters that are not in `order`
        for char in s_count:
            if char not in order_index:
                result.append(char * s_count[char])
        
        return ''.join(result)
