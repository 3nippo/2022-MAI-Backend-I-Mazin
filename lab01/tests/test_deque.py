import context
from lru_cache import Deque, Node

def assert_all(it1, it2):
    for a, b in zip(it1, it2):
        assert a.value == b

def test_push_front_empty():
    deque: Deque = Deque()

    deque.push_front(1)

    assert_all(deque, [1])
    assert deque.count == 1

def test_push_back_empty():
    deque: Deque = Deque()

    deque.push_back(1)

    assert_all(deque, [1])
    assert deque.count == 1

def test_push_back_conseq():
    deque: Deque = Deque()

    deque.push_back(1)
    deque.push_back(2)
    deque.push_back(3)

    assert_all(deque, [1, 2, 3])
    assert deque.count == 3

def test_push_front_conseq():
    deque: Deque = Deque()

    deque.push_front(1)
    deque.push_front(2)
    deque.push_front(3)

    assert_all(deque, [3, 2, 1])
    assert deque.count == 3

def test_remove_head():
    deque: Deque = Deque()

    head: Node = deque.push_back(1)
    deque.push_back(2)
    deque.push_back(3)
    
    deque.remove(head)

    assert_all(deque, [2, 3])
    assert deque.count == 2

def test_remove_tail():
    deque: Deque = Deque()

    deque.push_back(1)
    deque.push_back(2)
    tail: Node = deque.push_back(3)
    
    deque.remove(tail)

    assert_all(deque, [1, 2])
    assert deque.count == 2

def test_remove_middle():
    deque: Deque = Deque()

    deque.push_back(1)
    middle: Node = deque.push_back(2)
    deque.push_back(3)
    
    deque.remove(middle)

    assert_all(deque, [1, 3])
    assert deque.count == 2

def test_remove_to_empty():
    deque: Deque = Deque()
    
    values: list[int] = [1, 2, 3]
    nodes: list[Node] = []

    for value in values:
        nodes.append(deque.push_back(value))
    
    for node in nodes:
        deque.remove(node)

    assert_all(deque, [])
    assert deque.count == 0

def test_push_front_after_remove_to_empty():
    deque: Deque = Deque()

    node: Node = deque.push_front(1)

    deque.remove(node)

    deque.push_front(1)

    assert_all(deque, [1])
    assert deque.count == 1

def test_push_back_after_remove_to_empty():
    deque: Deque = Deque()

    node: Node = deque.push_back(1)

    deque.remove(node)

    deque.push_back(1)

    assert_all(deque, [1])
    assert deque.count == 1

def test_pop_back():
    deque: Deque = Deque()

    deque.push_back(1)
    deque.push_back(2)

    node: Node = deque.pop_back()
    
    assert node.value == 2
    assert_all(deque, [1])
    assert deque.count == 1

def test_pop_front():
    deque: Deque = Deque()

    deque.push_back(1)
    deque.push_back(2)

    node: Node = deque.pop_front()
    
    assert node.value == 1
    assert_all(deque, [2])
    assert deque.count == 1

def test_pop_back_to_empty():
    deque: Deque = Deque()
    
    deque.push_front(1)
    node: Node = deque.pop_back()
    
    assert node.value == 1
    assert_all(deque, [])
    assert deque.count == 0

def test_pop_front_to_empty():
    deque: Deque = Deque()
    
    deque.push_front(1)
    node: Node = deque.pop_front()
    
    assert node.value == 1
    assert_all(deque, [])
    assert deque.count == 0
