from __future__ import annotations # lol
import typing # omegalol
from collections import namedtuple

class Node:
    def __init__(
        self, 
        value: typing.Any,
        prev: typing.Optional[Node]=None, 
        next: typing.Optional[Node]=None
    ) -> None:
        self.value = value
        self.prev = prev
        self.next = next

    def remove(self) -> None:
        if self.prev:
            self.prev.next = self.next

        if self.next:
            self.next.prev = self.prev

        self.next = self.prev = None

    @staticmethod
    def connect(prev: Node, next: Node):
        next.prev = prev
        prev.next = next
        

class Deque:
    def __init__(self) -> None:
        self.head: typing.Optional[Node] = None
        self.tail: typing.Optional[Node] = None
        self.count: int = 0
        self._iter: typing.Optional[Node] = None
    
    def __iter__(self) -> Deque:
        self._iter = self.head
        return self

    def __next__(self) -> Node:
        if not self._iter:
            raise StopIteration

        next: Node = self._iter

        self._iter = self._iter.next
        
        return next

    def push_back(self, value: typing.Any) -> Node:
        self.count += 1
        new_node: Node = Node(value)

        if self.tail:
            Node.connect(self.tail, new_node)
        
        self.tail = new_node

        if not self.head:
            self.head = new_node

        return new_node

    def push_front(self, value: typing.Any) -> Node:
        self.count += 1
        new_node: Node = Node(value)

        if self.head:
            Node.connect(new_node, self.head)
        
        self.head = new_node

        if not self.tail:
            self.tail = new_node

        return new_node

    def pop_front(self) -> Node:
        assert self.head, "don't pop from empty deque"
        self.count -= 1

        head: Node = self.head

        self.head = self.head.next

        head.remove()

        if not self.head:
            self.tail = None

        return head

    def pop_back(self) -> Node:
        assert self.tail, "don't pop from empty deque"
        self.count -= 1

        tail: Node = self.tail

        self.tail = self.tail.prev

        tail.remove()

        if not self.tail:
            self.head = None

        return tail

    def remove(self, node: Node) -> None:
        """
            It is assumed 'node' is contained in deque
        """
        if self.head is node:
            self.pop_front()
        elif self.tail is node:
            self.pop_back()
        else:
            self.count -= 1
            node.remove()


KeyValuePair = namedtuple('KeyValuePair', ['key', 'value'])


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._cache = {}
        self._deque = Deque()

    def get(self, key: str) -> typing.Optional[str]:
        cached: typing.Optional[Node] = self._cache.get(key)
        
        if cached:
            self.remove(key)
            self.set(key, cached.value.value)
            return cached.value.value

        return None

    def set(self, key: str, value: str) -> None:
        if key in self._cache:
            self.remove(key)

        prepended: Node = self._deque.push_front(KeyValuePair(key, value))

        self._cache[key] = prepended

        if self._deque.count > self.capacity:
            node: Node = self._deque.pop_back()
            self.remove(node.value.key)


    def remove(self, key: str) -> None:
        cached: typing.Optional[Node] = self._cache.get(key)
        
        assert cached, "no value for key='{}'".format(key)

        self._deque.remove(cached)

        self._cache.pop(key)
