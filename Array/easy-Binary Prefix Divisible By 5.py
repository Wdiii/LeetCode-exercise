# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def prefixesDivBy5(self, A):
        #A: List[int]) -> List[bool]:
        res=[]
        a=""
        for i in range(len(A)):
            a+=str(A[i])
            res.append(int(a,2)%5==0)
        return res
        