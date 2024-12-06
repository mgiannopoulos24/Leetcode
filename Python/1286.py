from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # Generate all combinations of the given length and store them as a list
        self.combinations = list(combinations(characters, combinationLength))
        # Use an index to keep track of the current combination
        self.index = 0

    def next(self) -> str:
        # Get the next combination, convert tuple to string, and increment the index
        result = ''.join(self.combinations[self.index])
        self.index += 1
        return result

    def hasNext(self) -> bool:
        # Check if there are more combinations left
        return self.index < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()