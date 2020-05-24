# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=[""]
        for i in S:
            if i==stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
