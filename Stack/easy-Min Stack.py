# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._elem = []

    def push(self, x: int) -> None:
        self._elem.append(x)

    def pop(self) -> None:
        return self._elem.pop()

    def top(self) -> int:
        return self._elem[-1]

    def getMin(self) -> int:
        return min(self._elem)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()