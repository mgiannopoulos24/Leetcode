import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.element_to_indices = defaultdict(set)
        self.elements = []

    def insert(self, val: int) -> bool:
        # Append the element to the list
        self.elements.append(val)
        # Add the index of this element in the indices set
        self.element_to_indices[val].add(len(self.elements) - 1)
        # Return True if this is the first occurrence of val
        return len(self.element_to_indices[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.element_to_indices[val]:
            return False
        
        # Get the index of the element to remove
        remove_index = self.element_to_indices[val].pop()
        last_element = self.elements[-1]
        
        # Swap the element to remove with the last element
        self.elements[remove_index] = last_element
        if remove_index < len(self.elements) - 1:
            self.element_to_indices[last_element].remove(len(self.elements) - 1)
            self.element_to_indices[last_element].add(remove_index)
        
        # Remove the last element from the list
        self.elements.pop()
        
        # Clean up the dictionary if no more occurrences
        if not self.element_to_indices[val]:
            del self.element_to_indices[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)
