# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def pancakeSort(self, A):
        #A: List[int]) -> List[int]:
        n=len(A)
        res=[]
        for x in range(n,0,-1):
            i=A.index(x)
            res.append(i+1)
            res.append(x)
            A=A[:i:-1]+A[:i]
        return res
