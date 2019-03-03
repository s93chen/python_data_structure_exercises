class CircularQueue:

    ''' Queue implemeowtation using circularly linked list.

        Example: round-robin scheduler for allocating slices
                 of CPU time to multiple applications running
                 concurrently.
    '''

    class _Node:

        __slots__ = '_data', '_next'

        def __init__(self, data, next):
            self._data = data
            self._next = next

        def __str__(self):
            return '< Node data: {} >'.format(self._data)

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        ''' Return first element at the front of the queue '''

        if self.is_empty():
            raise Exception('Queue is empty')

        head = self._tail._next
        return head._data

    def dequeue(self):
        ''' Remove and return first element of the queue '''

        if self.is_empty():
            raise Exception('Queue is empty')

        old_head = self._tail._next

        if self._size == 1:
            self._tail = None
            print('Queue is now empty.')

        else:
            new_head = old_head._next
            self._tail._next = new_head

        self._size -= 1
        return old_head._data

    def enqueue(self, item):
        ''' Add an item to the end of the queue '''

        new_node = self._Node(item, None)

        if not self.is_empty():
            new_node._next = self._tail._next
            self._tail._next = new_node

        self._tail = new_node
        self._size += 1

    def rotate(self):
        ''' Rotate front node to end of queue
            i.e. old head becomes new tail
        '''

        if self._size > 0:
            self._tail = self._tail._next

if __name__ == '__main__':

    cq = CircularQueue()

    cq.enqueue('jackson')
    cq.enqueue('ella')
    cq.enqueue('udon')
    cq.enqueue('bun')

    print('Size of queue: {}'.format(len(cq)))
    print('First in the queue: {}'.format(cq.first())

    #cq.rotate()
    #print('Now servicing: {}'.format(cq.first()))
