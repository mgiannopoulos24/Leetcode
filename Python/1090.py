class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # Combine values and labels into a list of tuples and sort by value in descending order
        items = sorted(zip(values, labels), reverse=True, key=lambda x: x[0])
        
        # Dictionary to keep track of how many times a label has been used
        label_count = {}
        
        # Initialize sum and the number of items selected
        total_sum = 0
        selected_items = 0
        
        # Iterate through the sorted items
        for value, label in items:
            # Check if we have reached the desired number of items
            if selected_items >= numWanted:
                break
            
            # Check if the label has been used within the useLimit
            if label_count.get(label, 0) < useLimit:
                # Add the value to the total sum
                total_sum += value
                # Increment the number of selected items
                selected_items += 1
                # Update the label usage count
                label_count[label] = label_count.get(label, 0) + 1
        
        return total_sum
