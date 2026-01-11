# https://leetcode.com/problems/lru-cache
# 30.11.2026
 

class Double_linked_list:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dumpy = Double_linked_list()
        self.map = {}
        self.last = None
        self.length = 0

    def _remove(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.last = node.prev

    def _add_back(self, node):
        if not self.last:
            self.dumpy.next = node
            node.prev = self.dumpy
        else:
            self.last.next = node
            node.prev = self.last
        self.last = node
        node.next = None

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_back(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_back(node)
            return

        if self.length == self.capacity:
            lru = self.dumpy.next
            self._remove(lru)
            self.map.pop(lru.key)
        else:
            self.length += 1

        new_node = Double_linked_list(key, value)
        self.map[key] = new_node
        self._add_back(new_node)

