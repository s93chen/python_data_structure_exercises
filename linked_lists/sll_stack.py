
class SLL_Stack:

    ''' implemeowtation of Python stack ADT w/ SLL '''


    class _Node:

        ''' node for a SLL '''

        __slots__ = '_item', '_next'

        def __init__(self, item, next):
            self._item = item
            self._next = next


    def __init__(self):
        ''' init empty stack '''

        self._head = None
        self._size = 0

    def __len__(self):
        ''' no. of items in stack '''

        return self._size

    def is_empty(self):
        ''' return True if stack is empty '''

        return self._size == 0

    def top(self):
        ''' return item at head if not empty (not removed) '''

        if self.is_empty():
            raise Exception('Empty stack!')

        return self._head._item

    def push(self, elem):
        ''' push element to stack '''

        self._head = self._Node(elem, self._head)
        self._size += 1

    def pop(self):
        ''' return and remove head if not empty '''

        if self.is_empty():
            raise Exception('Nothing to pop other than your cherry.')

        res = self._head._item
        self._head = self._head._next
        self._size -= 1

        return res
