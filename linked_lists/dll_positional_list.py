
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

class PositionalList(_DoublyLinkedList):

    class Position:

        def __init__(self, container, node):

            '''
            Constructor for Position, not to be called by user

            Arguments:
                container: a positional list
                node: a node in/out of container
            '''

            self._container = container
            self._node = node

        def data(self):
            ''' Returns data of node at given position '''

            return self._node._data

        def __eq__(self, other):
            ''' Returns True when two positions refer to same node '''

            return type(self) == type(other) and self._node is other._node


        def __ne__(self, other):
            ''' Returns True when two positions refer to diff node '''

            return not (self == other)

    def _validate(self, p):
        ''' Returns node at p if position p is valid '''

        if not isinstance(p, self.Position):
            raise TypeError('p must be an instance of Position')

        if p._container is not self:
            raise ValueError('Position p is not in this positional list')

        if p._node._next is None:
            raise ValueError('p is no longer valid')

        return p._node

    def _make_position(self, node):
        ''' Wraps node into Position and returns it (None of sentinel) '''

        if (node is self._header) or (node is self._trailer):
            return None
        else:
            return self.Position(self, node)

    def first(self):
        ''' Returns Position of front of list (None if empty) '''

        return self._make_position(self._header._next)

    def last(self):
        ''' Returns Position of last of list (None if empty)'''

        return self._make_position(self._trailer._prev)

    def before(self, p):
        ''' Returns Position before p '''

        p_node = self._validate(p)
        return self._make_position(p_node._prev)

    def after(self, p):
        ''' Returns Position after p '''

        p_node = self._validate(p)
        return self._make_position(p_node._next)

    def __iter__(self):
        ''' Generates a forward iteration of the data in the list '''

        cur = self.first()
        while cur is not None:
            yield cur.data()
            cur = self.after(cur)

    def _insert_between(self, item, prev_node, next_node):
        ''' Overrides the inherited method. Returns new Position '''

        new_node = super()._insert_between(item, prev_node, next_node)
        return self._make_position(new_node)

    def add_first(self, item):
        ''' Insert item to front of the list and return new Position '''

        return self._insert_between(item, self._header, self._header._next)

    def add_last(self, item):
        ''' Insert item to end of the list and return new Position '''

        return self._insert_between(item, self._trailer._prev, self._trailer)

    def add_before(self, p, item):
        ''' Insert item before p and return new Position '''

        p_node = self._validate(p)
        return self._insert_between(item, p_node._prev, p_node)

    def add_after(self, p, item):
        ''' Insert item after p and return new Position '''

        p_node = self._validate(p)
        return self._insert_between(item, p_node, p_node._next)

    def replace(self, p, item):
        ''' Replace node at p with item and return replaced item '''

        p_node = self._validate(p)
        p_data = p_node._data
        p_node._data = item
        return p_data

    def delete(self, p):
        ''' Remove and return the element at position p '''

        p_node = self._validate(p)
        return self._delete_node(p_node)
