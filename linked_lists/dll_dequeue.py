
class _DoublyLinkedList:
    '''Implemeowtation for doubly linked list'''

    class _Node:

        __slots__ = '_data', '_prev', '_next'

        def __init__(self, data=None, prev=None, next=None):
            self._data = data
            self._prev = prev
            self._next = next

        def __str__(self):
            return '<node data: {}>'.format(self._data)

    def __init__(self):
        ''' Empty list with header and trailer pointing to each other '''

        self._header = self._Node()
        self._trailer = self._Node()
        self._header._next = self._trailer
        self._trailer._next = self._header
        self._size = 0

    def __len__(self):
        ''' Returns size of list '''

        return self._size

    def is_empty(self):
        ''' Returns True if list is empty'''

        return self._size == 0

    def _insert_between(self, item, prev_node, next_node):
        ''' Add item between two existing nodes, return reference
            to newly inserted node.
        '''

        new_node = self._Node(item, prev_node, next_node)
        prev_node._next = new_node
        next_node._prev = new_node
        self._size += 1

        return new_node

    def _delete_node(self, node):
        ''' Delete non-sentinel node from list and return its data '''

        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        # to return data
        data = node._data

        # deprecate node
        # helps python GC
        node._prev = None
        node._next = None
        node._data = None

        return data


class LinkedDequeue(_DoublyLinkedList):
    ''' Implemeowtation of a double-ended queue with DLL '''

    def first(self):
        ''' Return (not remove) item at front of queue '''

        if self.is_empty():
            raise Exception('Empty queue!')

        return self._header._next._data

    def last(self):
        ''' Return (not remove) item at end of queue '''

        if self.is_empty():
            raise Exception('Empty queue!')

        return self._trailer._prev._data

    def enqueue_front(self, item):
        ''' Enqueue at front of queue '''

        predecessor = self._header
        successor = self._header._next

        self._insert_between(item, predecessor, successor)

    def enqueue_back(self, item):
        ''' Enqueue at end of queue '''

        successor = self._trailer
        predecessor = self._trailer._prev

        self._insert_between(item, predecessor, successor)

    def dequeue_front(self):
        ''' Dequeue at front of queue and return data '''

        if self.is_empty():
            raise Exception('Empty queue!')

        front = self._header._next

        return self._delete_node(front)

    def dequeue_back(self):
        ''' Dequeque at end of queue and return data '''

        if self.is_empty():
            raise Exception('Empty queue!')

        back = self._trailer._prev

        return self._delete_node(back)


if __name__ == '__main__':

    q = LinkedDequeue()

    q.enqueue_front('jackson')
    q.enqueue_back('ella')
    q.enqueue_front('udon')
    q.enqueue_back('bun')

    print('first: {}'.format(q.first()))
    print('last: {}'.format(q.last()))

    q.dequeue_front()
    q.dequeue_back()

    print('first: {}'.format(q.first()))
    print('last: {}'.format(q.last()))
