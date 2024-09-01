class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Remove a node from the doubly linked list."""
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _add(self, node: Node) -> None:
        """Add a node right after the dummy head."""
        prev, next = self.head, self.head.next
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key: int) -> int:
        """Return the value of the key if the key exists, otherwise return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Update the value of the key if it exists. Otherwise, add the key-value pair to the cache."""
        if key in self.cache:
            # Update the value of the existing node
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used (tail's previous node)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

            # Add the new node to the cache and the linked list
            new_node = Node(key, value)
            self._add(new_node)
            self.cache[key] = new_node
