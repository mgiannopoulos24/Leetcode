import random

class RandomizedSet:

    def __init__(self):
        self.elements = []
        self.index_map = {}
        
    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        # Add the value to the list and map
        self.index_map[val] = len(self.elements)
        self.elements.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        # Get the index of the element to be removed
        idx = self.index_map[val]
        last_element = self.elements[-1]
        
        # Swap the element to remove with the last element
        self.elements[idx] = last_element
        self.index_map[last_element] = idx
        
        # Remove the last element from the list and dictionary
        self.elements.pop()
        del self.index_map[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)

