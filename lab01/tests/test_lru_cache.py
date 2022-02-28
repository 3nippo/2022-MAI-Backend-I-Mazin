import context
from lru_cache import LRUCache

def test_capacity():
    cache: LRUCache = LRUCache(2)

    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Tuco', 'Salamanca')

    assert cache.get('Jesse') == None

def test_items_present():
    cache: LRUCache = LRUCache(2)

    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')

    assert cache.get('Jesse') == 'Pinkman'
    assert cache.get('Walter') == 'White'

def test_bubble():
    cache: LRUCache = LRUCache(2)

    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.get('Jesse')
    cache.set('Tuco', 'Salamanca')
    
    assert cache.get('Walter') == None
    assert cache.get('Jesse') == 'Pinkman'
