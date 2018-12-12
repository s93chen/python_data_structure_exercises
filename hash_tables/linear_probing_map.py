from map_base import HashMapBase

class ProbeHashMap(HashMapBase):
    ''' hash map with linear probing as collision resolution '''

    _AVAIL = object()  # marks locations of prev deletions
