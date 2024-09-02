class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.count = {}
        self.freq_count = {}
        self.count_nodes = {}
        self.min_node = None
        self.max_node = None

    def _add_node(self, count):
        if count not in self.count_nodes:
            new_node = Node(count)
            self.count_nodes[count] = new_node
            if self.min_node is None:
                self.min_node = new_node
                self.max_node = new_node
            else:
                prev_node = self.max_node
                while prev_node and prev_node.count > count:
                    prev_node = prev_node.prev
                if prev_node is None:
                    new_node.next = self.min_node
                    self.min_node.prev = new_node
                    self.min_node = new_node
                else:
                    new_node.prev = prev_node
                    new_node.next = prev_node.next
                    if prev_node.next:
                        prev_node.next.prev = new_node
                    prev_node.next = new_node
                    if self.max_node == prev_node:
                        self.max_node = new_node
            self.freq_count[count] = new_node
        return self.count_nodes[count]

    def _remove_node(self, node):
        if node.keys:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.min_node:
            self.min_node = node.next
        if node == self.max_node:
            self.max_node = node.prev
        del self.count_nodes[node.count]
        del self.freq_count[node.count]

    def inc(self, key: str) -> None:
        old_count = self.count.get(key, 0)
        new_count = old_count + 1
        self.count[key] = new_count
        
        if old_count > 0:
            old_node = self.freq_count[old_count]
            old_node.keys.remove(key)
            if not old_node.keys:
                self._remove_node(old_node)
        
        new_node = self._add_node(new_count)
        new_node.keys.add(key)

    def dec(self, key: str) -> None:
        old_count = self.count[key]
        new_count = old_count - 1
        
        if old_count == 1:
            del self.count[key]
        else:
            self.count[key] = new_count
        
        old_node = self.freq_count[old_count]
        old_node.keys.remove(key)
        if not old_node.keys:
            self._remove_node(old_node)
        
        if new_count > 0:
            new_node = self._add_node(new_count)
            new_node.keys.add(key)

    def getMaxKey(self) -> str:
        if self.max_node:
            return next(iter(self.max_node.keys))
        return ""

    def getMinKey(self) -> str:
        if self.min_node:
            return next(iter(self.min_node.keys))
        return ""
