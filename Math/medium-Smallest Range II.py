# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def smallestRangeII(self, A, K):
        #A: List[int], K: int) -> int:
        A.sort()
        if len(A)==1:
            return 0
        else:
            res=A[-1]-A[0]
            for i in range(1,len(A)):
                Amin=min(A[0]+K,A[i]-K)
                Amax=max(A[-1]-K,A[i-1]+K)  
                res=min(Amax-Amin,res)
            return res
