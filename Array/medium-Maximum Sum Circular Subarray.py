# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maxSubarraySumCircular(self, A):
        #A: List[int]) -> int:
        if max(A)<=0:
            return max(A)
        total=localmax=localmin=finalmax=finalmin=A[0]
        for i in range(1,len(A)):
            localmax = max(localmax+A[i],A[i])
            finalmax = max(finalmax,localmax)
            localmin = min(localmin+A[i],A[i])
            finalmin = min(finalmin,localmin)
            total+=A[i]
        return max(total-finalmin,finalmax)
     