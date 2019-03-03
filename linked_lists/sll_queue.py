
class SLL_Queue:

    ''' implemeowtation of Python queue ADT w/ SLL '''


    class _Node:

        ''' node for a SLL '''

        __slots__ = '_item', '_next'

        def __init__(self, item, next):
            self._item = item
            self._next = next


    def __init__(self):
        ''' init empty queue '''

        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        ''' return size of queue '''

        return self._size

    def is_empty(self):
        ''' return True if empty '''

        return self._size == 0

    def first(self):
        ''' return first in queue if not empty '''

        if self.is_empty():
            raise Exception("Nothing. For. You.")

        return self._head._item

    def enqueue(self, elem):
        ''' add elem to end of queue '''

        new_node = self._Node(elem, None)

        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node

        self._tail = new_node
        self._size += 1

    def dequeue(self):
        ''' remove and return first item in queue '''

        if self.is_empty():
            raise Exception("Empty as an IoT kid's brain")

        res = self._head._item
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return res
