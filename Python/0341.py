from typing import List

# Definition of the NestedInteger class for context
class NestedInteger:
    def isInteger(self) -> bool:
        pass
    
    def getInteger(self) -> int:
        pass
    
    def getList(self) -> List['NestedInteger']:
        pass

class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        # Initialize the stack with the given nested list
        self.stack = list(reversed(nestedList))
    
    def _flatten(self):
        # Flatten the stack so that the top element is an integer if possible
        while self.stack and not self.stack[-1].isInteger():
            top_list = self.stack.pop().getList()
            self.stack.extend(reversed(top_list))
    
    def next(self) -> int:
        self._flatten()
        # The top of the stack is guaranteed to be an integer if hasNext() is called
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        self._flatten()
        return bool(self.stack) and self.stack[-1].isInteger()
