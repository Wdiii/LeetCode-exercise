# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def calPoints(self, ops):
        #ops: List[str]) -> int:
        stack=[]
        for i in ops:
            if i=="C":
                stack.pop()
            elif i=="D":
                stack.append((stack[-1])*2)
            elif i=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
        