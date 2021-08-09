import unittest

from misc.lru_cache import MyLRUCache


class LRUCacheTests(unittest.TestCase):

    def test_something(self):
        cache = MyLRUCache(3)
        cache.put(1,"dog")
        cache.put(3,"cat")

        print(cache)

        self.assertEqual(cache.capacity, 3)
        self.assertEqual(cache.get(2), -1)


if __name__ == '__main__':
    unittest.main()
