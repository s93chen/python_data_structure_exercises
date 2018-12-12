from map_base import HashMapBase
from unsorted_map import SimpleUnsortedMap

class ChainHashMap(HashMapBase):
    ''' hash map with separate chaining for collision resolution '''

    def _bucket_getitem(self, bkt_idx, k):
        bkt = self._table[bkt_idx]
        if bkt is None:
            raise KeyError("Key Error: " + repr(k))

        return bkt[k]

    def _bucket_setitem(self, bkt_idx, k, v):
        if self._table[bkt_idx] is None:
            self._table[bkt_idx] = SimpleUnsortedMap()

        prev_size = len(self._table[bkt_idx])
        self._table[bkt_idx][k] = v

        if len(self._table[bkt_idx]) > prev_size:
            self._size += 1

    def _bucket_delitem(self, bkt_idx, k):
        bkt = self._table[bkt_idx]
        if bkt is None:
            raise KeyError("Key Error: " + repr(k))

        del bkt[k]

    def __iter__(self):
        for bkt in self._table:
            if bkt is not None:
                for key in bucket:
                    yield key
