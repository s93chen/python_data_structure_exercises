"""
Problem:
Design a class which supports the stack operations push and pop. It must also
support an extra operation, max, which returns the largest element. You may
assume that the methods only deals with integer arguments.

Hints:
* You don't have to implement your own stack. Lists can be used as stacks via
  their append and pop methods.

Links:
https://docs.python.org/3.1/tutorial/datastructures.html#using-lists-as-stacks
https://docs.python.org/3.1/tutorial/datastructures.html#using-lists-as-queues
"""
"""
class MaxStack:

    def __init__(self):
        pass
    
    def push(self, value):
        pass

    def pop(self):
        pass

    def max(self):
        pass
"""
class MaxStack:

    def __init__(self):
        self._stack = []
        self._max = []

    def push(self, value):
        self._stack.append(value)

        if not self._max:
            self._max.append(value)
        elif value >= self._max[-1]:
            self._max.append(value)

    def pop(self):
        if not self._stack:
            print("Stack is empty.")
        else:
            top = self._stack.pop()
            if top == self._max[-1]:
                self._max.pop()
            return top

    def max(self):
        if not self._stack:
            print("Stack is empty.")
        else:
            return self._max[-1]

if __name__ == "__main__":
    stk = MaxStack()
    stk.push(2)
    stk.push(10)
    stk.push(3)
    stk.push(15)
    stk.push(15)
    print(stk.pop())
    print(stk.max())
    print(stk.pop())
    print(stk.max())
    print(stk.pop())
    print(stk.max())
    print(stk.pop())
    print(stk.max())
