from map_base import MapBase

class SimpleUnsortedMap(MapBase):
    ''' simple map with unsorted list '''

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value

        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return

        new = self._item(k, v)
        self._table.append(new)

    def __delitem__(self, k):
        for i in range(len(self._table)):
            if k == self._table[i]._key:
                self._table.pop(i)
                return

        raise KeyError("Key Error: " + repr(k))

    def __iter__(key):
        for item in self._table:
            yield item._key
