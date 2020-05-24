# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def buildArray(self, target, n):
        #target: List[int], n: int) -> List[str]:
        stack,res=[],[]
        for i in range(1,n+1):
            if i in target:
                stack.append(i)
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
            if stack==target:
                break
        return res