import collections

class LruCache:

    def __init__(self, capacity: int) -> None:
        self._isbn_price_table : collections.OrderedDict[int, int] = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn: int) -> int:
        if isbn not in self._isbn_price_table:
            return -1

        price = self._isbn_price_table.pop(isbn)

        # Update the looked up item to be the most recently used
        self._isbn_price_table[isbn] = price

        return price

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) == self._capacity:
            # Remove the element at the front of the queue, which
            # is the least recently used item
            self._isbn_price_table.popitem(last=False)

        self._isbn_price_table[isbn] = price

    def erase(self, isbn: int) -> bool:
        return self._isbn_price_table.pop(isbn, None) is not None




def main():
   cache = LruCache(2)
   cache.insert(12345, 10)
   cache.insert(23456, 100)
   cache.insert(34567, 1000)

   assert cache.lookup(12345) == -1
   assert cache.lookup(23456) == 100
   assert cache.erase(23456)
   assert not cache.erase(11111)

   print("All assertions passed")



if __name__ == "__main__":
    main()
