# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._elems = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._elems.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._elems.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._elems[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self._elems==[]


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
