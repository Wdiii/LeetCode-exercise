# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def minDominoRotations(self, A, B):
        #A: List[int], B: List[int]) -> int:
        n=len(A)
        res=[]
        for i in range(1,7):
            flag=0
            for j in range(n):
                if A[j]!=i and B[j]!=i:
                    flag=1
                    break
            if flag==0:
                res.append(i)
        if not res:
            return -1
        rotation=[]
        for k in res:
            rotation.append(min(n-A.count(k),n-B.count(k)))
        return min(rotation)
