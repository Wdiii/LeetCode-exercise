# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1,stack2=[],[]
        for i in S:
            if stack1 and i=="#":
                stack1.pop()
            elif i!='#':
                stack1.append(i)
        for j in T:
            if stack2 and j=="#":
                stack2.pop()
            elif j!='#':
                stack2.append(j)
        return stack1==stack2
        