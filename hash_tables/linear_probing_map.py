from map_base import HashMapBase

class ProbeHashMap(HashMapBase):
    ''' hash map with linear probing as collision resolution '''

    # place holder in available slot
    # that marks previous deletion
    _AVAIL = object()

    def _is_available(self, bkt_idx):
        ''' check if slot is available '''

        return (self._bkt_arr[bkt_idx] is None) or
               (self._bkt_arr[bkt_idx] is ProbeHashMap._AVAIL)

    def _find_slot(self, bkt_idx, k):
        ''' search for key k at given bucket

            returns (sucess, index), where:
                if found, success = True, index = bkt_idx
                if not, success = False, index = first_avail_slot
        '''

        first_avail_slot = None

        while True:

            # COMBAK:
            if self._is_available(bkt_idx):
                if first_avail_slot is None:
                    first_avail_slot = bkt_idx
                if self._bkt_arr(bkt_idx) is None:
                    return (False, first_avail_slot)

            elif k == self._bkt_arr[bkt_idx]._key:
                return (True, bkt_idx)

            bkt_idx = (bkt_idx + 1) % len(self._bkt_arr)

    def _bucket_getitem(self, bkt_idx, k):
        found, loc = self._find_slot(bkt_idx, k)

        if not found:
            raise KeyError("Key Error: " + repr(k))
        return self._bkt_arr[loc]._value

    def _bucket_setitem(self, bkt_idx, k, v):
        found, loc = self._find_slot(bkt_idx, k)

        if found:
            self._bkt_arr[loc]._value = v
        else:
            self._bkt_arr[loc] = self._item(k, v)
            self._size += 1

    def _bucket_delitem(self, bkt_idx, k):
        found, loc = self._find_slot(bkt_idx, k)

        if not found:
            raise KeyError("Key Error: " + repr(k))
        self._bkt_arr[loc] = ProbeHashMap._AVAIL

    def __iter__(self):
        for i in range(len(self._bkt_arr)):
            if not self._is_available(i):
                yield self._bkt_arr[i]._key
