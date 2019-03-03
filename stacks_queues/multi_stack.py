"""
Problem:

You must build a stack-like data structure, except it must be composed of
multiple actual stacks. The size of the internal stacks should be configurable
by the multi-stack constructor.

Operations to support include push, pop, size and pop_at. The first three are
the usual stack operations. The last method means pop an element from the ith
stack (and then re-arrange the elements in the internal stacks so that all
stacks have stk_cap elements except the last one). First implement the first
three methods, then you will see how to do the fourth.

As usual, raise an appropriate exception on an invalid pop or index.
"""


from collections import defaultdict

class MultiStack:

    def __init__(self, stk_cap):
        if stk_cap <= 0:
            raise ValueError('stk_cap must be greater than 0.')

        self._stk = defaultdict(list)
        self._cap = stk_cap
        self._idx = [0]
        self._size = 0
        self._stk[0]

    def __len__(self):
        return self._size

    def indices(self):
        return self._idx

    def push(self, x):
        self._size += 1
        top = self._idx[-1]
        if len(self._stk[top]) < self._cap:
            self._stk[top].append(x)
        else:
            self._stk[top + 1].append(x)
            self._idx.append(top + 1)

    def pop(self):
        if self._size == 0:
            raise IndexError('Stack is empty')

        self._size -= 1
        top = self._idx[-1]
        res = self._stk[top].pop()
        if (not self._stk[top]) and top != 0:
            del self._stk[top]
            self._idx.pop()

        return res

    def pop_at(self, i):
        top = self._idx[-1]
        if i not in self._idx:
            e = "i must be in range [0, {}]".format(top)
            raise IndexError("Stack index out of bound. " + e)

        self._size -= 1
        res = self._stk[i].pop()

        if i < top:
            for idx in range(i, top):
                tmp = self._stk[idx+1][0]
                self._stk[idx].append(tmp)
                del self._stk[idx+1][0]

        if not self._stk[top]:
            del self._stk[top]
            self._idx.pop()

        return res


if __name__ == "__main__":

    m = MultiStack(3)

    m.push(1)
    m.push(2)
    m.push(3)
    m.push(4)
    m.push(5)
    m.push(6)
    m.push(7)
    m.push(8)
    m.push(9)
    print(m._stk)       # {0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]}
    print(m.indices())  # [0, 1, 2]

    m.pop_at(0)         # return 3 | {0: [1, 2, 4], 1: [5, 6, 7], 2: [8, 9]}
    m.pop_at(1)         # return 7 | {0: [1, 2, 4], 1: [5, 6, 8], 2: [9]}
    m.pop_at(2)         # return 9 | {0: [1, 2, 4], 1: [5, 6, 8]}
    print(m._stk)       # {0: [1, 2, 4], 1: [5, 6, 8]}
    print(m.indices())  # [0, 1]

    m.pop()             # return 8 | {0: [1, 2, 4], 1: [5, 6]}
    m.pop()             # return 6 | {0: [1, 2, 4], 1: [5]}
    m.pop()             # return 5 | {0: [1, 2, 4]}

    print(len(m))       # 3
    print(m._stk)       # {0: [1, 2, 4]}
