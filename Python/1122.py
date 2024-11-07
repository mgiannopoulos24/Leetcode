class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a hashmap to store the position of each element in arr2
        order_map = {value: index for index, value in enumerate(arr2)}
        
        # Custom sort function
        def custom_sort_key(x):
            # If the element is in arr2, return its position in arr2
            if x in order_map:
                return (0, order_map[x])  # (0, index in arr2) to sort by arr2's order
            # If the element is not in arr2, return (1, x) to sort it naturally at the end
            return (1, x)
        
        # Sort arr1 using the custom key
        return sorted(arr1, key=custom_sort_key)
