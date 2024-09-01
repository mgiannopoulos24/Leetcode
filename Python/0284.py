class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked_value = None
        
        # Initialize the peeked value if there are elements in the iterator
        if self.iterator.hasNext():
            self.peeked_value = self.iterator.next()
            self.has_peeked = True
        else:
            self.has_peeked = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.peeked_value

    def next(self):
        """
        :rtype: int
        """
        if not self.has_peeked:
            raise Exception("No elements left")
        
        next_value = self.peeked_value
        self.has_peeked = self.iterator.hasNext()
        if self.has_peeked:
            self.peeked_value = self.iterator.next()
        else:
            self.peeked_value = None
        
        return next_value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_peeked
