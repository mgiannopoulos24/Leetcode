import random
from typing import List, Optional

class Node:
    def __init__(self, val: int, level: int):
        self.val = val
        self.forward = [None] * (level + 1)  # Levels are 0-indexed

class Skiplist:
    def __init__(self):
        self.MAX_LEVEL = 16
        self.P = 0.5
        self.head = Node(-1, self.MAX_LEVEL)
        self.level = 0
        random.seed(0)  # Fixed seed for deterministic behavior during testing

    def random_level(self) -> int:
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].val < target:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.val == target

    def add(self, num: int) -> None:
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        lvl = self.random_level()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.head
            self.level = lvl
        new_node = Node(num, lvl)
        for i in range(lvl + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current and current.val == num:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1
            return True
        else:
            return False