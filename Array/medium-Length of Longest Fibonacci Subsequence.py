# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:47:06 2020

@author: Di Wang
"""

class Solution:
    def lenLongestFibSubseq(self, A):
        #A: List[int]) -> int:
        S=set(A)
        res=0
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                count=2
                a,b=A[i],A[j]
                while a+b in S:
                    count+=1
                    a,b=b,a+b
                    res=max(res,count)
        return res if res > 2 else 0
                