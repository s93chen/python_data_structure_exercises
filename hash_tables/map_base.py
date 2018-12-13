from random import randrange
from collections import MutableMapping


class MapBase(MutableMapping):
    ''' map ABC with nested nonpublic class _item '''

    class _item:

        '''
        map items that stores key-value pairs,
        item comparisons are key-based.
        '''

        __slot__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other) # calls __eq__

        def __lt__(self, other):
            return self._key < other._key


class HashMapBase(MapBase):

    ''' map ABC using hash table and MAD compression fcn,
        where MAD the multiply-and-division method is defined as

            int i -> [(ai + b) mod p] mod N, where
                N = size of bucket array
                p = a prime number greater than N
                a = scale factor
                b = shift factor
    '''

    def __init__(self, cap=11, p=109345121):

        # hash table setup
        self._bkt_arr = [None] * cap
        self._cap = cap
        self._size = 0

        # MAD function
        self._a = 1 + randrange(p - 1)
        self._b = randrange(p)
        self._p = p

    def _hash_function(self, k):
        hc = hash(k)
        return ((self._a * hc + self._b) % self._p) % len(self._bkt_arr)

    def __len__(self):
        return self._size

    def __getitem__(self, k):
        bkt_idx = self._hash_function(k)
        return self._bucket_getitem(bkt_idx, k)

    def __setitem__(self, k, v):
        bkt_idx = self._hash_function(k)
        self._bucket_setitem(bkt_idx, k, v)

        cur_cap = len(self._bkt_arr)
        load_fctr = self._size / cur_cap

        if load_fctr > 0.5:
            self._resize(2 * cur_cap - 1)

    def __delitem__(self, k):
        bkt_idx = self._hash_function(k)
        self._bucket_delitem(bkt_idx, k)
        self._size -= 1

    def _resize(self, new_cap):
        '''
        resize bucket array to new cap, iterate through
        original array to copy over existing items
        '''

        old_arr = list(self.items())
        self._bkt_arr = [None] * new_cap
        self._cap = new_cap

        for (k, v) in old_arr:
            self[k] = v

    def _bucket_getitem(self, bkt_idx, k):
        raise NotImplementedError

    def _bucket_setitem(self, bkt_idx, k, v):
        raise NotImplementedError

    def _bucket_delitem(self, bkt_idx, k):
        raise NotImplementedError
