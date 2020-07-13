# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maxSumTwoNoOverlap(self, A, L, M):
        #A: List[int], L: int, M: int) -> int:
        res=0
        if L<M:
            L,M=M,L
        for i in range(len(A)-L+1):
            s1=sum(A[i:i+L])
            for j in range(i+L,len(A)-M+1):
                s2=sum(A[j:j+M])
                res=max(s1+s2,res)
            for k in range(i-M+1):
                s2=sum(A[k:k+M])
                res=max(s1+s2,res)
        return res