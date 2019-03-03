"""
Problem:
Design a class which supports the queue operations add and remove. However, it
must be implemented using two stacks!

Tips:
On an error condition (removing from empty queue) raise an IndexError.
"""

class MyQueue:

    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def add(self, value):
        self._stack1.append(value)

    def remove(self):
        if not (self._stack1 or self._stack2):
            raise IndexError('Removing from empty queue')

        # if stack2 is empty
        if self._stack1 and (not self._stack2):
            for item in self._stack1:
                temp = self._stack1.pop()
                self._stack2.append(temp)

        result = self._stack2.pop()
        return result
