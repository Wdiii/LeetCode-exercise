# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maxRotateFunction(self, A):
        #A: List[int]) -> int:
        #F(i) = F(i-1) + sum - n * A[n-i]
        c,f=0,0
        s=sum(A)
        for i in A:
            f+=c*i
            c+=1
        res=f
        for i in range(len(A)-1,0,-1):
            f= f+s-len(A)*A[i]
            res=max(res,f)
        return res 